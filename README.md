# Email Outreach Automation

## Overview
This project documents a Python-based workflow used to clean, merge, validate, and prepare outreach contact data for a real email campaign. The work was originally developed in Jupyter while consolidating participant records from multiple spreadsheets collected across several years.

This repository presents the main technical components of the process in a cleaner and more readable form.

## Project Scope
The project involved:

- consolidating contact data from multiple Excel files
- cleaning inconsistent schemas across years
- combining names and email addresses into a unified contact list
- removing duplicate and malformed entries
- validating email addresses using regex and DNS MX record checks
- preparing a final outreach list for batch delivery
- sending personalized HTML emails in batches through SendGrid

## Technical Highlights
- Used `pandas` to merge and clean multiple yearly datasets
- Standardized inconsistent column names such as `Email` vs `Email Address`
- Built validation checks for both email syntax and domain MX records
- Created a final cleaned contact list for outreach use
- Used SendGrid to send personalized HTML emails while accounting for authentication issues and sending limits

## Repository Structure
- `src/validate_emails.py` – regex and MX-record-based email validation utilities
- `src/send_emails.py` – batch email sending utilities using SendGrid
- `data/sample_input/` – sanitized example input data
- `data/sample_output/` – sanitized example output data

## Workflow Summary
1. Load participant spreadsheets from multiple years
2. Remove irrelevant columns and missing entries
3. Standardize contact fields across datasets
4. Merge records into one contact list
5. Remove duplicate email addresses
6. Validate addresses using syntax and MX checks
7. Export a final cleaned list
8. Send outreach emails in batches

## Notes
This repository contains a cleaned and simplified version of the work. Sensitive data such as real contact lists, private names, and API credentials are not included.

## Tools
- Python
- pandas
- Jupyter
- SendGrid API
- dnspython
- regex
