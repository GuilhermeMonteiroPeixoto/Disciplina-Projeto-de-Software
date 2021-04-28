from ..Model import EventHistory
import ManageEmployee
import ManageTransaction


class ManageHistoric:
    def __init__(self, manage_transaction: ManageTransaction, manage_employee: ManageEmployee):
        self._actual_uid = 0
        self._event_history: EventHistory = []
        self._manage_transaction = manage_transaction
        self._manage_employee = manage_employee

    def Undo(self):
        if self._actual_uid < len(self._event_history) - 1:
            self._actual_uid += 1
        # do undo pro redo so muda o +=1 ou -=1

    def Redo(self):
        if 0 < self._actual_uid - 1:
            self._actual_uid -= 1

        # All add
        if self._event_history[self._actual_uid].command == "add":
            if self._event_history[self._actual_uid].data_type == "Transaction":
                self._manage_transaction.add(self._event_history.old_data)

            elif self._event_history[self._actual_uid].data_type == "Employee":
                self._manage_employee.add(self._event_history.old_data)

        # All update
        if self._event_history[self._actual_uid].command == "update":
            if self._event_history[self._actual_uid].data_type == "Transaction":
                self._manage_transaction.update(self._event_history.old_data)

            elif self._event_history[self._actual_uid].data_type == "Employee":
                self._manage_employee.add(self._event_history.old_data)

        # ..
