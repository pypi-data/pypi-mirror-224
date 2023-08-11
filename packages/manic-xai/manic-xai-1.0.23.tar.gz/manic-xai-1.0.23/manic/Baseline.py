import numpy as np

class Baseline:
    """
    Baseline class for selecting counterfactuals from a set of base counterfactuals.

    @param disagreement: The Disagreement object used for calculating disagreement measures.
    @type disagreement: Disagreement

    @param base_counterfactuals: The base counterfactual instances.
    @type base_counterfactuals: list of list of int

    @param data_instance: The original data instance for which counterfactuals are being generated.
    @type data_instance: list of int

    @param labels: The base counterfactual labels.
    @type labels: list of str
    """
    def __init__(self, disagreement, base_counterfactuals, data_instance, labels):
        self.disagreement = disagreement
        self.base_counterfactuals = base_counterfactuals
        self.data_instance = data_instance
        self.labels = labels
    
    def __str__(self):
        """
        Return a string representation of the Baseline object.

        @return: String representation of the Baseline object.
        @rtype: str
        """
        return f"Baseline Object:\n" \
               f"Disagreement: {self.disagreement}\n" \
               f"Base Counterfactuals: {self.base_counterfactuals}\n" \
               f"Data Instance: {self.data_instance}"

    def to_string(self):
        """
        Convert the Baseline object to a string.

        @return: String representation of the Baseline object.
        @rtype: str
        """
        return self.__str__()

    def most_proximal_counterfactual(self):
        """
        Find the most proximal counterfactual instance based on proximity score.

        @return: The most proximal counterfactual instance and it's label.
        @rtype: list of int, str
        """
        best_proximity = float('inf')
        best_counterfactual = None
        best_counterfactual_label = None

        for counterfactual, label in zip(self.base_counterfactuals, self.labels):
            proximity = self.disagreement.calculate_proximity(self.data_instance, counterfactual)

            if proximity < best_proximity:
                best_proximity = proximity
                best_counterfactual = counterfactual
                best_counterfactual_label = label
        
        return best_counterfactual, best_counterfactual_label
    
    def most_agreeable_counterfactual(self):
        """
        Find the most agreeable counterfactual instance based on disagreement score. 

        @return: The most agreeable counterfactual instance and it's label.
        @rtype: list of int, str
        """
        best_disagreement = float('inf')
        best_counterfactual = None
        best_counterfactual_label = None

        for counterfactual, label in zip(self.base_counterfactuals, self.labels):
            disagreement = self.disagreement.calculate_disagreement(self.data_instance, counterfactual)

            if disagreement < best_disagreement:
                best_disagreement = disagreement
                best_counterfactual = counterfactual
                best_counterfactual_label = label
        
        return best_counterfactual, best_counterfactual_label
    
    def most_sparse_counterfactual(self):
        """
        Find the most sparse counterfactual instance based on sparsity score. 

        @return: The most sparse counterfactual instance and it's label.
        @rtype: list of int, str
        """
        best_sparsity = float('inf')
        best_counterfactual = None
        best_counterfactual_label = None

        for counterfactual, label in zip(self.base_counterfactuals, self.labels):
            sparsity, _ = self.disagreement.calculate_sparsity(counterfactual)

            if sparsity < best_sparsity:
                best_sparsity = sparsity
                best_counterfactual = counterfactual
                best_counterfactual_label = label
        
        return best_counterfactual, best_counterfactual_label
    
    def average_counterfactual(self):
        """
        Find the average ranked counterfactual instance based on sparsity, proxmity and disagreement score. 

        @return: The ranked average counterfactual instance and it's label.
        @rtype: list of int, str
        """
        sparsity_scores = [self.disagreement.calculate_sparsity(counterfactual) for counterfactual in self.base_counterfactuals]
        proximity_scores = [self.disagreement.calculate_proximity(self.data_instance, counterfactual) for counterfactual in self.base_counterfactuals]
        disagreement_scores =  [self.calculate_disagreement(counterfactual) for counterfactual in self.base_counterfactuals]

        sparsity_ranking = np.argsort(sparsity_scores) + 1
        proximity_ranking = np.argsort(proximity_scores) + 1
        disagreement_ranking = np.argsort(disagreement_scores) + 1
        
        average_ranking = np.mean([sparsity_ranking, proximity_ranking, disagreement_ranking], axis=0)
        best_counterfactual_index = np.argmin(average_ranking)

        return self.base_counterfactuals[best_counterfactual_index], self.labels[best_counterfactual_index]
    
    def calculate_disagreement(self, counterfactual):
        total_disagreement = 0
        
        for base_counterfactual in self.base_counterfactuals:
            disagreement = self.disagreement.calculate_disagreement(base_counterfactual, counterfactual)
            total_disagreement =+ disagreement
        
        avg_disagreement = total_disagreement / len(self.base_counterfactuals)

        return avg_disagreement