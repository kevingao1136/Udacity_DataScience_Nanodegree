# Starbucks Capstone Challenge

## Introduction
Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). The project represents a one-month experiment for Starbucks to test out the market and see what offers really excite different demographics of people.

A blog post of this project can be found here: https://medium.com/@kevingao1136/starbucks-capstone-challenge-a9e506509016

## Motivation
The purpose of this project is to determine which demographic groups respond best to which offer types, to help Starbucks make better decisions on sending out offers to targeted customers to increase sales and potentially save money.

By sending offers to the RIGHT customers
- Starbucks can boost brand recognition, customer loyalty, increase sales activities, promote a new product, etc.

By NOT sending offers to the RIGHT customers
- Starbucks can save costs on the promotion event on customers who would make purchases without offers
- Starbucks can prevent customers from reacting negatively to an offer by not sending the offer

## Example

To give an example, a user could receive a discount offer buy 10 dollars get 2 off on Monday. The offer is valid for 10 days from receipt. If the customer accumulates at least 10 dollars in purchases during the validity period, the customer completes the offer.

However, there are a few things to watch out for in this data set. Customers do not opt into the offers that they receive; in other words, a user can receive an offer, never actually view the offer, and still complete the offer. For example, a user might receive the "buy 10 dollars get 2 dollars off offer", but the user never opens the offer during the 10 day validity period. The customer spends 15 dollars during those ten days. There will be an offer completion record in the data set; however, the customer was not influenced by the offer because the customer never viewed the offer.

# Data
The datasets contain simulated data that mimics customer behavior on the Starbucks rewards mobile app.

There are three files of datasets:
- portfolio.json — containing offer ids and metadata about each offer (duration, type, etc.)
- profile.json — demographic data for each customer
- transcript.json — records for transactions, offers received, offers viewed, and offers completed

I have renamed each dataset for earlier interpretations. Here is the schema and explanation of each variable in the datasets:
**offers (portfolio.json)**
- id (string) — offer id
- offer_type (string) — type of offer i.e., BOGO, discount, informational
- min_spend (int) — minimum required spend to complete an offer
- reward (int) — reward given for completing an offer
- expire_days (int) — time for offer to be expired, in days
- channels (list of strings)

**customers (profile.json)**
- age (int) — age of the customer
- became_member_on (int) — date when customer created an app account
- gender (str) — gender of the customer (note some entries contain ‘O’ for other rather than M or F)
- id (str) — customer id
- income (float) — customer’s income

**events (transcript.json)**
- event (str) — record description (ie transaction, offer received, offer viewed, etc.)
- customer_id (str) — customer id
- hour (int) — time in hours since start of test. The data begins at time t=0
- value — (dict of strings) — either an offer id or transaction amount depending on the record


