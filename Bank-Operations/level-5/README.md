# Level 5 - Bank Incident Response

## Linux Bank Operations Lab

---

# Overview

Congratulations, Bank IT Technician!

You have completed the previous levels:

- Linux navigation  
- File permissions  
- Security investigations  
- Process recovery  

You are now assigned as the lead technician for a major bank security incident.

The bank's monitoring system has detected multiple problems across its Linux infrastructure.

This is the final challenge.

You must investigate the incident, secure the system, remove threats, repair damaged files, and submit a final incident report.

---

# Learning Objectives

By completing this lab, you will practice:

- Investigating Linux security incidents
- Searching logs for suspicious activity
- Managing file permissions
- Finding and stopping processes
- Repairing configuration files
- Organizing incident evidence
- Creating professional documentation

---

# Commands You Will Use

You may need:

```bash
ls
cd
cat
grep
find
chmod
ps
kill
nano
cp
mv
Important Concepts
Security Investigation

Linux administrators often investigate incidents by reviewing:

System logs
Running processes
File permissions
Configuration files

The goal is to identify what happened and restore the system.

Getting Started

## Step 1 - Create the Lab

Navigate to the Level 5 folder.

Run:

python3 create_lab.py

The setup script will:

Ask for your employee name
Create the bank incident environment
Generate security logs
Create compromised files
Start suspicious processes
Create the verification script

## Step 2 - Enter the Investigation Folder

Navigate into:

cd bank_incident
## Step 3 - Read Your Assignment

Open the incident task file:

cat incident_tasks.txt

The security department has provided your mission details.