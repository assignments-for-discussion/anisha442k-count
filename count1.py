def count_batteries_by_usage(cycles):
  for i in cycles:
    if (i <=149):
      print('lowCount')
    elif(i>=150 & i<=649):
      print('mediumCount')
    elif(i>649):
      print('highCount')
    else:
      exit
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
