from ..Controller.ManageEmployee import ManageEmployee
from ..Controller.ManageTransaction import ManageTransaction
from ..Controller.ManageCommons import ManageCommons


class ManageHistoric:
    def __init__(self, manageCompany, manageSyndicate, manageEmployee, manageExtraUnionFees, managePropertySale,
                   manageWorkingPoint, manageTransaction):
        self._max_historic = 0
        self._actual_historic = 0

        self._manageCompany = manageCompany
        self._manageSyndicate = manageSyndicate
        self._manageEmployee = manageEmployee
        self._manageExtraUnionFees = manageExtraUnionFees
        self._managePropertySale = managePropertySale
        self._manageWorkingPoint = manageWorkingPoint
        self._manageTransaction = manageTransaction

        self._manageCompany = [manageCompany.get_all()]
        self._manageSyndicate = [manageSyndicate.get_all()]
        self._manageEmployee = [manageEmployee.get_all()]
        self._manageExtraUnionFees = [manageExtraUnionFees.get_all()]
        self._managePropertySale = [managePropertySale.get_all()]
        self._manageWorkingPoint = [manageWorkingPoint.get_all()]
        self._manageTransaction = [manageTransaction.get_all()]


    def add(self):
        self._manageCompany = [manageCompany.get_all()]
        self._manageSyndicate = [manageSyndicate.get_all()]
        self._manageEmployee = [manageEmployee.get_all()]
        self._manageExtraUnionFees = [manageExtraUnionFees.get_all()]
        self._managePropertySale = [managePropertySale.get_all()]
        self._manageWorkingPoint = [manageWorkingPoint.get_all()]
        self._manageTransaction = [manageTransaction.get_all()]
    def undo(self):
        if self._actual_historic < len(self._event_history) - 1:
            self._actual_historic += 1
        return self._event_history[self._actual_historic]

    def redo(self):
        if 0 < self._actual_historic - 1:
            self._actual_historic -= 1
        return self._event_history[self._actual_historic]

    def save(self, event_history):
        self._event_history
