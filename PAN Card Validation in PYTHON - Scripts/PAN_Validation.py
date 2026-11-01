import pandas as pd
df = pd.read_excel('PAN Number Validation Dataset.xlsx')
print(df.head(10))
print('Total records = ',len(df))

# .str.strip() 删除首尾空格
df['Pan_Numbers'] = df['Pan_Numbers'].astype('string').str.strip().str.upper()
print(df.head(10))

print('\n')
print(df[df['Pan_Numbers'] == ''])
print(df[df['Pan_Numbers'].isna()])   #.isna()：检查真正的缺失值，例如 None、NaN、pd.NA

print(df['Pan_Numbers'].duplicated())
print(df['Pan_Numbers'].duplicated().sum())

#.dropna()：删除缺失值
print(df['Pan_Numbers'].dropna().duplicated().sum())
df_clean = df.drop_duplicates(subset=['Pan_Numbers'])
print(len(df_clean))
#.duplicated() → 检查重复，返回 True / False
#.drop_duplicates() → 删除重复，返回去重后的数据
df_clean = df_clean.dropna(subset=['Pan_Numbers'])
print(len(df_clean))

print((df_clean['Pan_Numbers'] == '').sum())  #output = 1
df_clean = df_clean[df_clean['Pan_Numbers'] != '']
print(len(df_clean))

###Data Validation### 10 characters
print(df_clean['Pan_Numbers'].str.len())
print(df_clean[df_clean['Pan_Numbers'].str.len() != 10])
print((df_clean['Pan_Numbers'].str.len() != 10).sum()) 
#长度错误的 PAN Number还需归类为 Invalid

print(df_clean['Pan_Numbers'].str.fullmatch(r'[A-Z]{5}[0-9]{4}[A-Z]'))
df_clean = df_clean.copy()
df_clean['Format_Valid'] = df_clean['Pan_Numbers'].str.fullmatch(r'[A-Z]{5}[0-9]{4}[A-Z]')
print(df_clean.head(10))
print(df_clean['Format_Valid'].sum())










##Adjacent Duplicate Letter CHECK
print(df_clean['Pan_Numbers'].str[:5])

def has_adjacent_duplicates(text): 
    for i in range(4):
        if text[i] == text[i+1]:
            return True
    return False
df_clean['has_adjacent_duplicates'] = df_clean['Pan_Numbers'].apply(has_adjacent_duplicates)
print(df_clean['has_adjacent_duplicates'].sum())

# consecutive letter(sequence) CHECK ↓  
def has_consecutive_letters(text):
    for i in range(4):
        if ord(text[i+1]) - ord(text[i]) != 1:
            return False
    return True
df_clean['has_consecutive_letters'] = df_clean['Pan_Numbers'].apply(has_consecutive_letters)
print(df_clean['has_consecutive_letters'].sum())

# four digits相邻重复
def has_adjacent_duplicate_digits(text):
    digits = text[5:9]
    if len(digits) != 4:
        return False
    
    for i in range(3):                  # compare 3 times
        if digits[i] == digits[i+1]:
            return True
    return False
df_clean['has_adjacent_duplicate_digits'] = df_clean['Pan_Numbers'].apply(has_adjacent_duplicate_digits)
print(df_clean['has_adjacent_duplicate_digits'].sum())

# four digits连续
def has_consecutive_digits(text):
    digits = text[5:9]
    if len(digits) != 4 or not digits.isdigit():
        return False

    for i in range(3):
        if int(digits[i+1]) - int(digits[i]) != 1:
            return False
    return True
df_clean['has_consecutive_digits'] = df_clean['Pan_Numbers'].apply(has_consecutive_digits)
print(df_clean['has_consecutive_digits'].sum())











### Categorisation                             ##  ~ NOT
df_clean['Is_Valid'] = (df_clean['Format_Valid'] & ~df_clean['has_adjacent_duplicates']
    & ~df_clean['has_consecutive_letters']
    & ~df_clean['has_adjacent_duplicate_digits']
    & ~df_clean['has_consecutive_digits']
)
print(df_clean[['Pan_Numbers', 'Is_Valid']].head(10))

valid_count = df_clean['Is_Valid'].sum()
invalid_count = (~df_clean['Is_Valid']).sum()
print("Valid PAN:", valid_count)
print("Invalid PAN:", invalid_count)



### 3186 Valid + 5839 Invalid = 9025，
print("Missing:", df['Pan_Numbers'].isna().sum())  # Missing PAN
print("Empty:", (df['Pan_Numbers'] == '').sum())  # Empty PAN
# Incomplete PAN          [lt(10) 就是 less than 10（长度小于 10）]
print("Incomplete:", df['Pan_Numbers'].dropna().str.len().lt(10).sum())

missing_or_incomplete = (
    df['Pan_Numbers'].isna()
    | df['Pan_Numbers'].str.len().lt(10).fillna(False)  # OR
)  # Missing or Incomplete PAN

print("Missing or Incomplete:", missing_or_incomplete.sum())




# print(df_clean)