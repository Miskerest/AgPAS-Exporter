import pandas as pd
import datetime
import re


# If you're reading this spaghetti code, I'm sorry!

def swap_names(name_string):
	delim = name_string.rfind(" ")
	first = name_string[:delim]
	last = name_string[delim+1:]
	return last + ", " + first
	

funded = "questionnaire_funded.csv"
nonfunded = "questionnaire_non_funded.csv" # hardcoded file paths- can be changed to be more flexible in finding these files
noi = "notice_of_intent_to_submit.csv"
outfile = "database_out.xlsx"

xlin = pd.read_csv(funded)
noi_xlin = pd.read_csv(noi)

rows_list = []
for i, row in xlin.iterrows():
	
	# date format: '2019-01-17 16:03:20'
	CREATED = row.get("Created")
	DEADLINE = row.get("Deadline")
	try:
		CREATED = pd.to_datetime(pd.to_datetime(CREATED, format="%Y-%m-%d %H:%M:%S", exact=False).strftime("%m/%d/%Y"))
	except:
		print("Unable to determine submission time from %s. Ensure YYYY-MM-DD HH:MM:SS format" % CREATED)

	try:
		DEADLINE = pd.to_datetime(pd.to_datetime(DEADLINE, format="%Y-%m-%d %H:%M:%S", exact=False).strftime("%m/%d/%Y"))
	except:
		print("Unable to determine deadline from %s. Ensure YYYY-MM-DD HH:MM:SS format" % DEADLINE)

	PI_ID = swap_names(row.get("Principal Investigator Name", default=''))
	DEPT_ID = row.get("Tenure Home Dept. Name")
	SPONSOR_ID = row.get("Sponsor/Agency NAME")
	AMOUNT = row.get("Total Requested Amount")
	MOU = ""
	COSTSHARE = row.get("Will you be including cost-share? (Must be required by sponsor)")
	TITLE = row.get("Proposal Title")
	COMMENTS = noi_xlin.get("Comments/Special Instructions")[i]
	KR_NUM = "FILL ME"

	rows_list.append([PI_ID, DEPT_ID, SPONSOR_ID, AMOUNT, MOU, "", "", CREATED, "", DEADLINE, "", COSTSHARE, "", "", TITLE, COMMENTS, KR_NUM])

out = pd.DataFrame(rows_list, columns=["PI_ID", "DEPT_ID", "SPONSOR_ID", "AMOUNT", "MOU", "ContinuationFRS", "ContinuationFRS#",  "DeliveredDate", "DeadlineDateType",
									   "DeadlineDate", "FY", "CostShare", "CostShareType", "CostShareDetails", "Title", "Comments", "KR Proposal #"])

while (True):
	try:
		out.to_excel(outfile, "Database")
		break
	except PermissionError: 

		ans = input("Unable to open %s for writing. Close the spreadsheet if it's open. Try again?\nY/n:" % outfile)
		if ('y' in ans or 'Y'in ans or ans.strip() == ""):
			continue
		else:
			break