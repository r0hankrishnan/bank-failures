#Modules
import pandas as pd

bank = pd.read_csv("./data/banklist.csv", encoding='windows-1254')
bfb = pd.read_csv("./data/bfb-all-data.csv", encoding='windows-1254')

bank.columns
#Merge right to match fewer rows (l = bank, r = bfb)
print(f"bank vs bfb shape: {bank.shape} vs {bfb.shape}")

BankName = bank.iloc[:,0]
ClosingDate = bank.iloc[:,5]

dropCols = [0,5]

bank = bank.drop(bank.columns[dropCols], axis = 1)

bank["BankName"] = BankName
bank["ClosingDate"] = ClosingDate

#Create copy of bfb
bfb1 = bfb.copy()

bfb1["Bank Name"] = bfb1['Bank Name, City, State'].apply(lambda x: x.strip().split(',')[0])

inner = pd.merge(bank, bfb1, how = "inner", left_on = ["BankName", "ClosingDate"], right_on = ["Bank Name", "Closing Date"])

inner.shape
inner.columns

dropCols = ["BankName", "ClosingDate", "Press Release (PR)", "Acquirer & Transaction"]
bankFailures = inner.drop(dropCols, axis = 1)

