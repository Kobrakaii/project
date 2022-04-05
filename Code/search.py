import pandas 


df = pandas.read_csv('books.csv')
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', 400)

def get_choice(data, column):

    
    nums = [val for val in range(len(df[column].unique()))]
    choices = list(zip(nums, df[column].unique()))
    print("Select '%s' of the car\n" % column)
    for v in choices:
        print("%s.  %s" % (v))
    user_input = input("Answer: ")
    user_answer = [val[1] for val in choices if val[0]==int(user_input)][0]
    print("'%s' = %s\n" % (column, user_answer))
    return user_answer

def main():

    make_input = get_choice(data=df, column="make")
    model_input = get_choice(data=df, column="model")
    year_input = get_choice(data=df, column="year")
    newdf = df.loc[(df["make"]==make_input)&(df["model"]==model_input)&(df["year"]==year_input)]
    print(newdf)

if __name__ == "__main__":
    main()