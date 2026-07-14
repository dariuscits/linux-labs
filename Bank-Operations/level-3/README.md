# Level 3 - Fraud Investigation

## Linux Bank Operations Lab

---

# Overview

Welcome back, Bank IT Technician!

After successfully securing the bank's vault, you have been assigned to assist the security investigation team.

The fraud department has detected suspicious activity across multiple bank systems. Several security alerts have been triggered, and the investigation team needs help analyzing system logs.

Your mission is to investigate the logs, identify suspicious activity, and create a report for the security team.

---

# Learning Objectives

By completing this lab, you will practice:

- Searching log files
- Filtering information
- Using Linux pipelines
- Counting and sorting data
- Analyzing security events
- Creating investigation reports

---

# Commands You Will Use

You may need:

```bash
grep
cat
less
head
tail
find
wc
sort
uniq
cut
|

# Prerequisites

Before starting this lab, you should understand:

- Basic Linux navigation
- Creating files and folders
- Reading text files
- Basic command-line usage

---

# Getting Started

## Step 1 - Create the Lab

Navigate to the Level 3 folder.

Run:

```bash
python3 create_lab.py

The setup script will:

Ask for your employee name
Create the bank investigation environment
Generate security log files
Create your investigation assignment
Create the verification script

##Step 2 - Enter the Investigation Folder

Navigate into the bank investigation directory:

cd bank_investigation

##Step 3 - Read Your Assignment

Open the investigation task file:

cat investigation_tasks.txt

The task file contains the instructions provided by the fraud department.