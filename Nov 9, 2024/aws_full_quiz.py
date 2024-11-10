import random

# Full list of concepts and definitions from your PDF
concepts = {
    "SageMaker Data Wrangler": "Data Preparation, Transformation, and feature engineering Tool with a single interface for data selection, cleaning, exploration, and processing.",
    "SageMaker Model Cards": "Record information about ML models including training details, evaluation metrics, and model performance.",
    "SageMaker Canvas": "Build ML models without needing to write any code.",
    "Amazon SageMaker Ground Truth": "Service that uses a human workforce to create accurate labels for data used in model training.",
    "SageMaker Model Monitor": "Automated alert system to monitor model quality, data drift, and anomalies over time.",
    "SageMaker Studio": "Suite of IDEs like JupyterLab and RStudio to build and manage ML models.",
    "Guardrails for Amazon Bedrock": "Evaluates user inputs and model responses based on policies, providing additional safeguards.",
    "Amazon Rekognition": "Fully managed AI service for image and video analysis with content moderation capabilities.",
    "AWS Artifact": "Audit resource for on-demand access to security and compliance documentation for AWS Cloud.",
    "AWS CloudTrail": "Tracks user activity and API usage, recording actions for audit purposes.",
    "Amazon CloudWatch": "Centralized logging service for monitoring AWS resources, application logs, and performance metrics.",
    "AWS Trusted Advisor": "Provides resources and recommendations for cost optimization, security, and resilience.",
    "Amazon Macie": "ML-powered service for monitoring and protecting sensitive data in Amazon S3.",
    "AWS Config": "Tracks AWS resource configurations to ensure compliance standards are met.",
    "Amazon DocumentDB": "Managed JSON document database with vector search support.",
    "Amazon OpenSearch Service": "Managed service for deploying, scaling, and operating OpenSearch, supports high query throughput and semantic search.",
    "SageMaker Clarify": "Provides explainability for models, evaluating biases and understanding model decisions.",
    "SageMaker JumpStart": "Hub with hundreds of pre-trained models, but user models can't be added.",
    "SageMaker Model Registry": "Managed catalog for managing model versions, metadata, and approvals.",
    "Embeddings": "Vector representations that capture semantic relationships for content with similar meanings.",
    "Amazon Inspector": "Vulnerability management for scanning EC2, Lambda, and ECR repositories.",
    "Amazon Comprehend": "NLP service for extracting insights from text, such as sentiment and key phrases.",
    "Amazon Textract": "Service for extracting text from documents, including handwritten text.",
    "Amazon Kendra": "Intelligent search service that provides answers based on contextual understanding.",
    "Amazon Q Business": "Generative AI virtual assistant for answering questions, summarizing, and generating content.",
    "Retrieval Augmented Generation (RAG)": "Optimizes language model output by referencing external knowledge sources.",
    "Fine Tuning": "Further training a pre-trained model on task-specific data to improve specificity and accuracy.",
    "Continued Pre-Training": "Ongoing training using industry-specific unlabeled data.",
    "Transfer Learning": "Reusing a model developed for one task as a starting point for a new task.",
    "Chain of Thought": "Prompt technique to break complex questions into smaller parts.",
    "Amazon Lex": "Managed AI service for conversational voice and text interfaces.",
    "Amazon Transcribe": "Converts speech to text.",
    "Amazon Polly": "Converts text to speech.",
    "Amazon Personalize": "Personalized product recommendations.",
    "Amazon Translate": "Translates text between 75 languages.",
    "Amazon Forecast": "Predicts future time series data points.",
    "Amazon Fraud Detector": "Detects fraud in transactions, product reviews, and payments.",
    "Bias": "Unfair prejudice or preference in data or model predictions.",
    "Fairness": "Impartial treatment without discrimination.",
    "Overfitting": "Model performs well on training data but poorly on new data.",
    "Underfitting": "Model is too simple to capture patterns in data.",
    "Explainability": "Understanding a model's decision-making process in human terms.",
    "Generative AI Model": "Creates novel, human-like outputs based on training data.",
    "ROUGE": "Metric for evaluating text summarization and machine translation quality.",
    "BLEU": "Metric for evaluating quality of machine-translated text.",
    "Top K": "Limits token selection to K most probable options in language models.",
    "Top P": "Limits word choice in language models to top percent of probability distribution.",
    "Temperature": "Controls diversity in model output by adjusting randomness.",
    "F1": "Metric balancing precision and recall for evaluating classification models.",
    "BERTScore": "Metric for semantic similarity between generated and reference text.",
    "Semantic Robustness": "Evaluates model output changes based on small input changes.",
    "Perplexity": "Measures how well a language model predicts test text.",
    "Accuracy": "Percentage of correct predictions.",
    "Precision": "True positives / (true positives + false positives).",
    "Recall": "True positives / (true positives + false negatives).",
    "False Positive Rate": "False positives / (false positives + true negatives).",
    "AUC-ROC": "Graph of recall over false positive rate; 1 indicates perfect accuracy.",
    "Mean Squared Error (MSE)": "Average squared differences between predicted and actual values.",
    "R Squared (R2)": "Percentage of variance explained by model.",
    "Root Mean Squared Error (RMSE)": "Square root of MSE, indicating model prediction error.",
    "Amazon Bedrock": "Managed service for accessing and integrating foundation models.",
    "Low Bias and Low Variance": "Ideal model training outcome with low erroneous assumptions and noise.",
    "Overfitting (Low Bias, High Variance)": "Model captures noise in data.",
    "Underfitting (High Bias, Low Variance)": "Model misses patterns in data.",
    "Hallucination": "AI response not justified by training data.",
    "Gen AI Architectures": "Includes GANs, VAEs, Transformers, Diffusion Models.",
    "GAN": "Network contest where one agent's gain is another's loss.",
    "VAE": "Generative algorithm that detects anomalies and removes noise.",
    "Transformers": "Model architecture that learns context in sequence data.",
    "AWS Audit Manager": "Continually audits AWS usage to simplify compliance.",
    "SageMaker Inference": "Options for deploying models on SageMaker, including real-time and batch inference.",
    "AWS AI Service Cards": "Resource for understanding AWS AI services.",
    "Amazon SageMaker Debugger": "Monitors and profiles model training in real-time.",
    "Amazon Augmented AI (Amazon A2I)": "Human review systems for ML predictions.",
    "Amazon SageMaker Autopilot": "Helps understand model predictions and characteristics.",
    "Epoch": "One training cycle through the dataset.",
    "AWS PrivateLink": "Provides private VPC connectivity to AWS services.",
    "Learning Rate": "Hyperparameter controlling model parameter update speed.",
    "Supervised Learning": "Learning from labeled data to map inputs to outputs.",
    "Unsupervised Learning": "Learning patterns from unlabeled data.",
    "Semi-Supervised Learning": "Mix of labeled and unlabeled data for improved model performance.",
    "Stop Sequences": "Specific tokens directing an AI model to stop generating.",
    "Intelligent Document Processing (IDP)": "Automates data entry from paper documents.",
    "Feature Extraction": "Creating new features from input data.",
    "Feature Selection": "Selecting the most relevant features for modeling.",
    "Multi-Class Classification": "Classification task with three or more classes.",
    "Multi-Label Classification": "Classification where each instance can belong to multiple classes.",
    "Amazon Bedrock Custom Model Import": "Enables importing custom models to Bedrock.",
    "Amazon Bedrock Knowledge Bases": "Provides context to foundation models using private data.",
}

# Function to create a quiz question
def generate_question():
    correct_concept = random.choice(list(concepts.keys()))
    correct_definition = concepts[correct_concept]

    # Prepare multiple choices
    choices = [correct_definition]
    while len(choices) < 4:
        random_definition = random.choice(list(concepts.values()))
        if random_definition not in choices:
            choices.append(random_definition)
    random.shuffle(choices)

    # Display the question and choices
    print(f"What is {correct_concept}?")
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    # Take user answer
    try:
        user_answer = int(input("Enter the number of your answer: "))
        if choices[user_answer - 1] == correct_definition:
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer was: {correct_definition}\n")
    except (ValueError, IndexError):
        print("Please enter a valid option.\n")

# Main function to run the quiz
def start_quiz():
    print("AWS Certified AI Practitioner Test Quiz")
    num_questions = int(input("How many questions would you like to answer? "))
    for _ in range(num_questions):
        generate_question()

# Run the quiz
start_quiz()
