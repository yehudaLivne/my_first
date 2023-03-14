def diff_avg(first_numbers_list,second_numbers_list):
  return sum([first_numbers_list[a]-second_numbers_list[a] for a in range(len(first_numbers_list))])/len(first_numbers_list)

def anti_bi(stringi):
  return [charcect for charcect in stringi if not charcect=='b']


def main():
  print(diff_avg([1,4,5],[0,0,4]))
  print(anti_bi('afdba'))


if __name__ == '__main__':
  main()