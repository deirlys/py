######################################################################
# Author: Una Ibrahimpasic
# Author: Dragan Babic
# Author: Edina Bojic
# Codes and decodes names so that we can work with numbers instead
# Numbers are faster, strings are slow and difficult to work with
######################################################################


class Coder:
    def __init__(self):
        self._week_cnt = 0
        self._week_desc = {}
        self._desc_week = {}
        self._files_cnt = []
        self._files_desc = []
        self._desc_files = []

    def encode_week(self, week):
        if week not in self._week_desc:
            self._week_desc[week] = self._week_cnt
            self._desc_week[self._week_cnt] = week
            self._week_cnt = self._week_cnt + 1
            self._files_cnt.extend([0])
            self._files_desc.append({})
            self._desc_files.append({})
        return self._week_desc[week]

    def encode(self, week, file):
        if week not in self._week_desc:
            # Register the week if it is not registered
            self._week_desc[week] = self._week_cnt
            self._desc_week[self._week_cnt] = week
            self._week_cnt = self._week_cnt + 1
            self._files_cnt.extend([0])
            self._files_desc.append({})
            self._desc_files.append({})
        week_index = self._week_desc[week]
        if file not in self._files_desc[week_index]:
            # Register the day if it isn't registered
            self._files_desc[week_index][file] = self._files_cnt[
                week_index]
            self._desc_files[week_index][
                self._files_cnt[week_index]] = file
            self._files_cnt[week_index] = self._files_cnt[
                                              week_index] + 1
        day_index = self._files_desc[week_index]
        return week_index, day_index[file]

    def print(self):
        #  This is used for debugging
        print("week - desc1 - desc2 - files - desc1 - desc2")
        print(self._week_cnt)
        print(self._week_desc)
        print(self._desc_week)
        print(self._files_cnt)
        print(self._files_desc)
        print(self._desc_files)
        print("\n")

    def decode(self, week_nr, day_nr):
        return self._desc_week[week_nr], self._desc_files[week_nr][
            day_nr]

    def decode_week(self, week_nr):
        return self._desc_week[week_nr]

    def encoded_weeks(self):
        return self._week_cnt

    def encoded_signs(self, week_nr):
        return self._files_cnt[week_nr]
