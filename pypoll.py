import csv
import os

file_to_load = os.path.join("Downloads/election_results.csv")
file_to_save = os.path.join("Downloads", "election_analysis.txt")

#writing csv
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)


# define variables
total_votes_cast = 0
list_of_candidates = []
candidate_votes = 0
winner_percentage = 0
votes_cast = 0
winner = ""
winning_count = []
candidates = row[2]
vote_percentage = 0

    for row in file_reader:
        total_votes_cast += 1
        candidates = row[2]
        if candidates != votes_cast:
            list_of_candidates.append(candidates)
            candidate_votes[candidates] += 1
        else:
            candidate_votes[candidates] = 1

    for candidate in list_of_candidates:
        votes = candidate_votes[candidate]
        vote_percentage = "{:.3%}".format(votes_cast/total_votes_cast)
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes_cast:,})\n")
        print(candidate_results)

        if (votes_cast > winning_count) and (vote_percentage > winner_percentage):
            winning_count = votes_cast
            winner = candidate
            winner_percentage = vote_percentage

            winner_summary = (
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winner_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winner_summary)




with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_cast:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    txt_file.write(candidate_results)
    txt_file.write(winner_summary)