# Email Outreach Automation

## Overview
This project automates email outreach by combining data cleaning, contact list consolidation, email validation, and batch delivery. The workflow was built in Python to process participant records collected across multiple years, generate a clean master contact list, and prepare personalized outreach emails for delivery through SendGrid.

## What the Project Does
- Loads and combines multiple contact datasets from Excel files
- Cleans inconsistent column formats and removes incomplete entries
- Merges records into a unified contact list
- Removes duplicate emails
- Validates email addresses using regex and DNS MX record checks
- Exports a finalized outreach dataset
- Sends personalized batch emails using the SendGrid API

## Technical Highlights
- Built a data processing pipeline in `pandas` for merging and cleaning contact data
- Standardized inconsistent schema across files (for example, `Email` vs `Email Address`)
- Implemented email validation using both syntax checks and domain-level MX record verification
- Added batch sending logic to work within SendGrid sending limits
- Used HTML email templating to improve formatting consistency

## Workflow
1. Load participant data from multiple yearly spreadsheets
2. Drop irrelevant columns and missing entries
3. Standardize email/name fields across datasets
4. Concatenate records into a single contact list
5. Remove duplicate addresses
6. Validate addresses using regex and MX record checks
7. Export the cleaned final list
8. Send personalized outreach emails in batches through SendGrid

## Tools
- Python
- pandas
- Jupyter Notebook
- SendGrid API
- regex
- dnspython

## Results
The final workflow produced a cleaned and validated outreach list from multiple source files and supported batch email delivery for a real outreach campaign.

## Notes
Sensitive data such as real email addresses, private contact lists, and API credentials have been removed from this public repository.

## Repository Structure
- `notebooks/` – development notebook for cleaning, validation, and sending workflow
- `data/sample_input/` – sanitized example input data
- `data/sample_output/` – sanitized example output data
- `report/` – short project notes and documentation

## Future Improvements
- Refactor notebook logic into reusable Python modules
- Add logging and retry handling for failed sends
- Add configurable templates and command-line execution
- Add automated tests for validation utilities
