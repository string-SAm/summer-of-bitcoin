import pandas

df = pandas.read_csv('mempool.csv', index_col='tx_id')


df['wbf'] = df.apply(lambda row: row.weight/row.fee, axis=1)
df = df.sort_values(by='wbf')
df.to_csv("operations.csv", index=True)

sorted_df = pandas.read_csv('operations.csv')
sorted_df.to_csv("operations.csv", index=True)


result = []
count = 0
fees = 0

for index, row in sorted_df.iterrows():
    if(isinstance(row['parents '], float)):
        if(count+row['weight'] < 4000000):
            result.append(row["tx_id"])
            count += row['weight']
            fees += row['fee']
        else:
            break

    else:
        for x in result:
            if(x == row["parents "]):
                if(count+row['weight'] < 4000000):
                    result.append(row["tx_id"])
                    count += row['weight']
                    fees += row['fee']
                else:
                    break


file1 = open("output.txt", "w")
for tx in result:
    file1.write(tx)
    file1.write('\n')
file1.write(str(fees))
file1.write('\n')
file1.write(str(count))
file1.close()
