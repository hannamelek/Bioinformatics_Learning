# Day 4 – Running BLASTP Against the NCBI Database

## Objective

Learn how to perform a remote BLASTP search against the NCBI non-redundant (nr) protein database, understand BLAST tabular output formats, and filter significant sequence matches using Linux command-line tools.

---
## Tasks Completed

* Ran a remote BLASTP search using the `-remote` option.
* Generated BLAST output in tabular format using `-outfmt 6`.
* Learned the meaning of the 12 columns in BLAST tabular output.
* Filtered significant hits based on E-value using `awk`.
* Generated BLAST output with column headers using `-outfmt 7`.

---

## Commands Used

```bash
# Run BLASTP remotely against the NCBI nr database
blastp -query mystery.fasta -db nr -remote \
-out results.txt -outfmt 6

# Display the BLAST results
cat results.txt

# Filter hits with E-value less than 0.001
awk '$11 < 0.001' results.txt > significant_hits.txt

# Run BLASTP with headers included
blastp -query mystery.fasta -db nr -remote \
-out results_headers.txt -outfmt 7

# Display the output with headers
cat results_headers.txt
```

---

## BLAST Output Format 6 Columns

| Column | Description                  |
| ------ | ---------------------------- |
| 1      | Query Sequence ID (qseqid)   |
| 2      | Subject Sequence ID (sseqid) |
| 3      | Percentage Identity          |
| 4      | Alignment Length             |
| 5      | Number of Mismatches         |
| 6      | Number of Gap Openings       |
| 7      | Query Start Position         |
| 8      | Query End Position           |
| 9      | Subject Start Position       |
| 10     | Subject End Position         |
| 11     | E-value                      |
| 12     | Bit Score                    |

---

## Understanding the E-value

The **E-value (Expectation Value)** estimates the number of matches expected to occur by chance when searching a database.

* Lower E-values indicate more significant matches.
* An E-value below **0.001** is generally considered statistically significant.

Example:

```bash
awk '$11 < 0.001' results.txt
```

This command prints only highly significant BLAST hits.

---

## Output Formats

### outfmt 6

* Tab-separated format.
* No headers.
* Easy to process with scripts and tools like `awk`, `cut`, or Python.

### outfmt 7

* Same tabular format as outfmt 6.
* Includes comment lines and column headers.
* Easier for humans to read and interpret.

---

## Expected Output Files

* `results.txt` — BLAST results in tabular format.
* `results_headers.txt` — BLAST results with descriptive headers.
* `significant_hits.txt` — Filtered results with E-value < 0.001.

---

## Note

The remote BLAST search could not be completed because the installed BLAST version did not support secure HTTPS communication (GNUTLS/TLS), preventing a connection to the NCBI servers. Although the search did not produce output files, the commands, workflow, output formats, and filtering methods were successfully studied and documented as part of the learning process.

---

## Learning Outcome

By completing this exercise, I learned how to:

* Perform remote BLASTP searches using the command line.
* Use different BLAST output formats.
* Interpret BLAST alignment statistics.
* Understand the significance of E-values.
* Filter BLAST results using Linux `awk`.
* Recognize and troubleshoot connection issues related to remote BLAST searches.
