from transaction import Transaction

trnsct_123 = Transaction()

#testcase 1
trnsct_123.add_item('Ayam Goreng', 2, 20_000)
trnsct_123.add_item('Pasta Gigi', 3, 15_000)

#testcase 2
trnsct_123.delete_item('Pasta Gigi')
trnsct_123.check_order()

#testcase 3
trnsct_123.reset_transaction()

#testcase 4
trnsct_123.add_item('Ayam Goreng', 2, 20_000)
trnsct_123.add_item('Pasta Gigi', 3, 15_000)
trnsct_123.add_item('Mainan Mobil', 1, 200_000)
trnsct_123.add_item('Mie Instant', 5, 3_000)
trnsct_123.check_order()
trnsct_123.total_price()

