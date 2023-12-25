from base import BaseXlsBlock
from datetime import datetime
from collections import defaultdict

class TopPayersBlock(BaseXlsBlock):
    NAME = "Отчёт по активным клиентам"

    def write_header(self):
        self.worksheet.write(self.row, self.col, self.NAME)

    def process_payments(self):
        quarterly_payments = defaultdict(lambda: defaultdict(float))
        for payment in self.data['payments']:
            client_id = payment['client_id']
            amount = payment['amount']
            created_at = datetime.strptime(payment['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
            quarter = (created_at.month - 1) // 3 + 1
            quarterly_payments[client_id][quarter] += amount
        return quarterly_payments

    def write_data(self):
        self.row += 1

        clients = self.data['clients']
        quarterly_payments = self.process_payments()

        top_payers = [{'client_id': client_id, 'total_amount': sum(data.values())} for client_id, data in quarterly_payments.items()]
        top_payers.sort(key=lambda x: x['total_amount'], reverse=True)
        top_payers = top_payers[:10]

        for i, payer in enumerate(top_payers, start=1):
            client_info = next(client for client in clients if client['id'] == payer['client_id'])
            fio = client_info['fio']
            
            
            last_name, first_name = fio.split(' ', 1)  

            
            self.worksheet.write(self.row + i, self.col, f"{i}. {last_name}")  
            self.worksheet.write(self.row + i, self.col + 1, first_name) 
            
            self.worksheet.write(self.row + i, self.col + 2, payer['total_amount'])

            
class TopCitiesBlock(BaseXlsBlock):
    NAME = "География клиентов"

    def write_header(self):
        self.worksheet.write(self.row, self.col, self.NAME)

    def write_data(self):
        self.row += 1

        clients = self.data['clients']

        city_counts = {}
        for client in clients:
            city = client['city']
            city_counts[city] = city_counts.get(city, 0) + 1

        top_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        for i, (city, count) in enumerate(top_cities, start=1):
            
            self.worksheet.write(self.row + i, self.col, f"{i}. {city}") 
            self.worksheet.write(self.row + i, self.col + 1, f"{count} клиентов")  


class AccountStatusBlock(BaseXlsBlock):
    NAME = "Анализ состояния счёта"

    def write_header(self):
        self.worksheet.write(self.row, self.col, self.NAME)

    def write_data(self):
        self.row += 1

        clients = self.data['clients']
        payments = self.data['payments']

        account_balances = {}
        for payment in payments:
            client_id = payment['client_id']
            amount = payment['amount']
            account_balances[client_id] = account_balances.get(client_id, 0) + amount

        top_balances = sorted(account_balances.items(), key=lambda x: x[1], reverse=True)[:10]

        for i, (client_id, balance) in enumerate(top_balances, start=1):
            client_info = next(client for client in clients if client['id'] == client_id)
            fio = client_info['fio']
            
            
            last_name, first_name = fio.split(' ', 1)  

       
            self.worksheet.write(self.row + i, self.col, f"{i}. {last_name}")  
            self.worksheet.write(self.row + i, self.col + 1, first_name) 
            self.worksheet.write(self.row + i, self.col + 2, f"Баланс - {balance}")  