# Extract Table from PDF (text)

## Introduction

This script utilizes the package Tabula and Camelot to extract potential tables from text PDF. The script will first use Camelot to extract and if Camelot's algorithm does not detect the table, it will use Tabula. Once all the tables are extracted and processed, it will be outputted into a single Excel with each table housed in the tab signifying the page of the PDF. 

* Further processing
  * There is a chance that some elements of Camelot's extracted table  is not accurate, so the script will look for delimiter "\n" and split it more accurately.

## How to use

* Main Packages
  * Camelot
  * Tabula (will need to ensure Java is in the Path)
