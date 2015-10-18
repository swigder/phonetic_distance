class PhoneticCostCalculator:
    """
    Cost calculator to calculate the difference between phones.  Considers distance between phones when calculating
    substitution cost.
    Phone similarities are based on the classification of phones as listed on Wikipedia.  See
    https://en.wikipedia.org/wiki/Arpabet for listing.
    """

    vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
    r_colored_vowels = ['ER', 'AXR']
    stops = ['P', 'B', 'T', 'D', 'K', 'G']
    affrictaves = ['CH', 'ZH']
    frictaves = ['F', 'V', 'TH', 'DH', 'S', 'Z', 'SH', 'ZH', 'HH']
    nasals = ['M', 'EM', 'N', 'EN', 'NG', 'ENG']
    liquids = ['L', 'EL', 'R', 'DX', 'NX']
    semivowels = ['Y', 'W', 'Q']

    phone_types = [vowels, r_colored_vowels, stops, affrictaves, frictaves, nasals, liquids, semivowels]

    def insertion_cost(self, phone):
        """
        Returns cost of inserting a given phone
        :param phone: the phone to be inserted
        :return: constant cost of 1 for any phone
        """
        return 1

    def deletion_cost(self, phone):
        """
        Returns cost of deleting a given phone
        :param phone: the phone to be deleted
        :return: constant cost of 1 for any phone
        """
        return 1

    def substitution_cost(self, phone1, phone2):
        """
        Returns cost of substituting any phone for another.  Considers similarities between phones to calculate
        substitution cost.
        :param phone1: the phone to be substituted
        :param phone2: the phone to substitute with
        :return: 0 if the phones are the same, 1 if the phones are alike, and 2 if the phones are different
        """
        if phone1 == phone2:
            return 0
        for phone_type in self.phone_types:
            phone1_of_type = phone1 in phone_type
            phone2_of_type = phone2 in phone_type
            if phone1_of_type and phone2_of_type:
                return 1
            if phone1_of_type or phone2_of_type:
                return 2
        raise Exception('Invalid phones provided.', phone1, phone2)