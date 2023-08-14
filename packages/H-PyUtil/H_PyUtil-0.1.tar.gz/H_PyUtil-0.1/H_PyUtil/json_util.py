import json
from loguru import logger

class DataManager:
    """
    A class for managing data storage with optional logging.

    Args:
        filename (str, optional): The name of the data file. Defaults to 'data.json'.
        write_logs (bool, optional): Determines whether logs should be written. Defaults to True.

    Attributes:
        filename (str): The name of the data file.
        data (dict): The loaded data stored in a dictionary.
        write_logs (bool): Indicates whether logs are being written.

    Methods:
        load_data() -> dict:
            Loads data from the specified file and returns it as a dictionary.

        save_data():
            Saves the current data dictionary to the file.

        get(key) -> Any:
            Retrieves the value associated with the given key from the data dictionary.

        set(key, value):
            Sets a key-value pair in the data dictionary and saves the data.

        update(new_data):
            Updates the data dictionary with the provided dictionary and saves the data.

        delete(key):
            Deletes a key-value pair from the data dictionary and saves the data.

    Example:
        # Create an instance of DataManager with logs enabled
        data_manager = DataManager(filename='data.json', write_logs=True)
        
        # Set data
        data_manager.set('name', 'John')
        
        # Get data
        name = data_manager.get('name')
        print(name)  # Output: John
    """


    def __init__(self, filename='data.json', write_logs=True):
        self.filename = filename
        self.data = self.load_data()
        self.write_logs = write_logs

        if self.write_logs:
            logger.add("logs.log", rotation="1 month", compression='zip')

    def load_data(self) -> dict:
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if self.write_logs:
                    logger.success("Файл успешно загружен")
        except FileNotFoundError:
            data = {}
            if self.write_logs:
                logger.warning("Файл не найден")
        except Exception as e:
            if self.write_logs:
                logger.error("Произошла ошибка: " + str(e))
        return data

    def save_data(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, ensure_ascii=False, indent=4)
                if self.write_logs:
                    logger.success("Файл успешно сохранен")
        except Exception as e:
            if self.write_logs:
                logger.error("Произошла ошибка: " + str(e))

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self.save_data()

    def update(self, new_data):
        self.data.update(new_data)
        self.save_data()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_data()
            if self.write_logs:
                logger.success(f"Запись с ключом '{key}' удалена")
        else:
            if self.write_logs:
                logger.warning(f"Запись с ключом '{key}' не найдена")