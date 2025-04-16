# This file contains configuration settings for the application, such as file paths, AI model parameters, and other constants used throughout the project.

class Config:
    # File paths
    BASE_DIR = "c:/Users/KIRTI/OneDrive/Desktop/once/"
    DATA_DIR = BASE_DIR + "data/"
    MODEL_DIR = BASE_DIR + "models/"
    
    # AI model parameters
    MODEL_NAME = "ai_model"
    TRAINING_EPOCHS = 100
    BATCH_SIZE = 32
    LEARNING_RATE = 0.001
    
    # Other constants
    LOGGING_LEVEL = "INFO"
    MAX_DIRECTORY_SIZE = 1000  # Maximum number of entries in the directory management system
    SUPPORTED_FILE_TYPES = ['.txt', '.csv', '.json']  # Supported file types for processing

    
class Settings:
    def __init__(self):
        # Initialize model parameters using Config constants
        self.model_parameters = {
            "max_depth": 5,
            "random_state": 42
        }
        self.learning_rate = Config.LEARNING_RATE
        self.batch_size = Config.BATCH_SIZE
        self.training_epochs = Config.TRAINING_EPOCHS
        self.supported_file_types = Config.SUPPORTED_FILE_TYPES