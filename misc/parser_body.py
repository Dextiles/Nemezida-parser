from typing import NoReturn
import misc.instruments


class Parser:
    def __init__(self, links) -> NoReturn:
        """
        Initializes the class with the provided links. Sets up logger,
        DataFrameCombiner, PhotoSave, and GetPerson instances.
        Parameters:
            links: The links to be used for initialization.
        Returns:
            None
        """
        self.__logger = misc.instruments.logger.Logger()
        self.__Combiner = misc.instruments.dataframe_combiner.DataFrameCombiner()
        self.__PhotoSave = misc.instruments.photo_save.PhotoSave()
        self.__PersonGet = misc.instruments.person_get.GetPerson()
        self.links = links
        self.is_data_get = False

    def parse(self) -> NoReturn:
        """
        Parses the links and retrieves person data for each link. If the data retrieval is successful,
        the data frame, links, and uid are extracted from the data. The data frame is added to the
        combiner, and the photos are saved using the PhotoSave class. If the data retrieval or photo
        saving fails, an appropriate log message is generated. If the data retrieval and photo saving
        are successful, the is_data_get flag is set to True. After parsing all the links, if the
        is_data_get flag is True, the data frame is saved to an Excel file using the FilesSaver class.
        If the saving to Excel is successful, an appropriate log message is generated. This function
        does not return any value.
        """
        for link in self.links:
            data = self.__PersonGet.get_person_data(link)
            if data is False:
                self.__logger.to_log('Парсинг данных', '..NO', link)
            else:
                self.__logger.to_log('Парсинг данных', '..OK', link)
                data_frame, links, uid = data
                if data_frame is not None:
                    self.__Combiner.add(data_frame)
                    if self.__PhotoSave.save_all(links, uid) is False:
                        self.__logger.to_log('Сохранение фото', '..NO', link)
                    else:
                        self.__logger.to_log('Сохранение фото', '..OK', link)
                        self.is_data_get = True
        if self.is_data_get:
            if misc.instruments.excel_file_worker.FilesSaver(self.__Combiner.data_frame).save() is False:
                self.__logger.to_log('Сохранение в Excel', '..NO')
            else:
                self.__logger.to_log('Сохранение в Excel', '..OK')
