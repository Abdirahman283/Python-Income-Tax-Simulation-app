from TP_Wise.service.canadaRevenueService import CanadaService
from TP_Wise.service.quebecRevenueService import QuebecService
from TP_Wise.persistence_layer.taxBracketDAO import TaxBracketDAO


class TaxWiseUI:

    def __init__(self):
        self.run()

    def run(self):
        dao = TaxBracketDAO()
        ca_service = CanadaService(dao)
        qc_service = QuebecService(dao)
        flag = True
        while flag:
            print("\nMENU:")
            print('='*40)
            print("1. Calculate tax amount")
            print("2. Display tax brackets by state")
            print("3. Quit")
            print('=' * 40)
            choice = int(input("Enter your choice (1/2/3): "))

            if choice == 1:
                amount = float(input("What is the income: "))
                authority = int(input("What is the authority(1:CANADA, 2:QUEBEC): "))

                if authority == 1:
                    tax_amount = ca_service.calculate_tax(amount)
                    print(F'     Federal tax is: {tax_amount:.2f} $')

                elif authority == 2:
                    tax_amount = qc_service.calculate_tax(amount)
                    print(F'     Provincial tax is: {tax_amount:.2f} $')

            elif choice == 2:
                authority = input("What is the authority (CA/QC):  ")
                if authority == 'CA':
                   print(f'Federal income tax rates:\n {ca_service.brackets_by_state('CA')}')


                elif authority == 'QC':
                    print(f'Quebec income tax rates:\n {qc_service.brackets_by_state('QC')}')

                else :
                    print("Invalid authority.\n Please choose (CA/QC).")

            elif choice == 3:
                print("Thanks for using our application")
                flag = False

            else:
                print("Invalid choice.\nPlease choose from the available options")


if __name__ == '__main__':
     TaxWiseUI()




