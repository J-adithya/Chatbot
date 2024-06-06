import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration, Trainer, TrainingArguments
from datasets import load_dataset, concatenate_datasets

def main():
    # Load datasets for AI, programming, and general knowledge
    code_search_net = load_dataset("code_search_net", "python", split="train[:5000]")
    ai2_arc = load_dataset("ai2_arc", "ARC-Challenge", split="train[:5000]")
    squad_v2 = load_dataset("squad_v2", split="train[:5000]")
    
    # Combine datasets and use a subset for quick training
    combined_dataset = concatenate_datasets([
        code_search_net.shuffle(seed=42).select(range(1000)),
        ai2_arc.shuffle(seed=42).select(range(1000)),
        squad_v2.shuffle(seed=42).select(range(1000)),
    ])

    # Load tokenizer and model
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

    # Tokenize dataset
    def tokenize_function(examples):
        if 'func_name' in examples and 'docstring' in examples:  # CodeSearchNet
            inputs = examples['func_name']
            outputs = examples['docstring']
        elif 'question' in examples and 'answerKey' in examples:  # AI2 ARC
            inputs = examples['question']
            outputs = examples['answerKey']
        elif 'question' in examples and 'answers' in examples:  # SQuAD v2
            inputs = examples['question']
            if examples['answers']['text']:  # Ensure there's at least one answer
                outputs = examples['answers']['text'][0]
            else:
                outputs = ""  # If no answer, use an empty string
        else:
            raise ValueError("Dataset format is not recognized")

        inputs = [str(input) for input in inputs]
        outputs = [str(output) for output in outputs]

        model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
        labels = tokenizer(outputs, max_length=128, truncation=True, padding="max_length")
        model_inputs['labels'] = labels['input_ids']
        return model_inputs

    num_proc = 8
    tokenized_dataset = combined_dataset.map(tokenize_function, batched=True, remove_columns=combined_dataset.column_names, num_proc=num_proc)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        overwrite_output_dir=True,
        num_train_epochs=5,  # Increase the number of epochs for better learning
        per_device_train_batch_size=4,  # Adjust batch size based on system capacity
        save_steps=10_000,
        save_total_limit=2,
        logging_dir="./logs",
        fp16=True,  # Enable mixed precision training
        evaluation_strategy="epoch",
    )

    # Define trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # Train the model
    trainer.train()

    # Evaluate the model
    eval_results = trainer.evaluate()
    print(f"Evaluation results: {eval_results}")

    # Save the model
    model.save_pretrained("./chatbot_model")
    tokenizer.save_pretrained("./chatbot_model")

if __name__ == "__main__":
    main()
