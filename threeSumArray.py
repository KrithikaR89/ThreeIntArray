""" Leetcode Q 15:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""

import datetime
import logging

format_used = logging.Formatter('%(asctime)s - %(lineno)d - %(message)s', datefmt='%D %I:%M:%Y %p')

log = logging.getLogger()
log.setLevel(logging.INFO)

streamer = logging.StreamHandler()
streamer.setFormatter(format_used)
streamer.setLevel(logging.INFO)
log.addHandler(streamer)

ts = datetime.datetime.now().strftime('%d-%m-%y_%I:%M:%S%p')
file_handle = logging.FileHandler(f'Result_log_{ts}.log')
file_handle.setFormatter(format_used)
file_handle.setLevel(logging.INFO)
log.addHandler(file_handle)

log.propagate = False


class ThreeSumArray:
    """ This class holds methods to calculate three zero sum array sets"""

    @staticmethod
    def find_three_sum_zero_sets(input_list):
        """
        This method find the sub-lists that make three sum zero arrays from input_list
        :param input_list: Master list with numbers
        :return:final_list : List containing sub sets of zero three sum
        """
        final_list = []

        if len(input_list) < 3 or not all(isinstance(element, int) for element in input_list):
            return []

        if len(input_list) >= 3:
            if all(element == 0 for element in input_list):
                return [[0, 0, 0]]
            elif input_list.count(0) >= 3:
                final_list.append([0, 0, 0])
            else:
                pass

        for i in range(len(input_list)):
            log.info(f'Testing element - {input_list[i]} at position {i}')
            for j in range(1, len(input_list)):
                if i+j < len(input_list):
                    number_to_track = input_list[i] + input_list[i+j]
                    log.info(f"Number to track is : {number_to_track}")
                    if number_to_track > 0:
                        number_of_concern = -abs(number_to_track)
                    elif number_to_track == 0:
                        number_of_concern = 0
                    else:
                        number_of_concern = abs(number_to_track)

                    log.info(f"Number of concern is : {number_of_concern}")

                    if number_of_concern in input_list and number_of_concern != input_list[i] \
                            and number_of_concern != input_list[i+j]:
                        index_of_found_number = input_list.index(number_of_concern)
                        if i != index_of_found_number and j != index_of_found_number:
                            zero_sum_list = sorted([input_list[i], input_list[i+j], number_of_concern])
                            log.info(f"Created a new zero sum list : {zero_sum_list}")

                            if zero_sum_list not in final_list:
                                log.info(f"Adding zero sum list {zero_sum_list} to final result")
                                final_list.append(zero_sum_list)

        return final_list


if __name__ == '__main__':
    trsm = ThreeSumArray()
    final_list = trsm.find_three_sum_zero_sets(input_list=[0, 0, 0, 0, 0])
    log.info(final_list)
