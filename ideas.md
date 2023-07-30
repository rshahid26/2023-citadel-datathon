# ideas
store airports as vertices, flight paths as edges with price weight


each edge can have a .name attribute leading to their respective airlines

traversing edges with a common airline gives edge induced subgraphs
that show which each airline travels to

I don't think "events" is too relevant

# datasets
### airlines
Mapping of airline IDs to names.

### airports
Important details (name, state, identifier, latitude, longitude, etc.) on various US airports.

### events_US
Public events from around the US throughout 2017.

### fares
Airline fare distributions for each quarter-route-airline combination in 2017 with a bucket size of $10.

### flight_traffic
Information about delays for US domestic flights in 2017.

### stock_prices
Daily closing stock prices of various US airlines from late-2016 to early-2018.

### weather
Weather data (temperature, wind, precipitation, cloud cover, etc.) collected at various US airports every 6
hours through 2017.

#scoring
● Technical Executive Summary

o Insightfulness of Conclusions. What is the question that your team set out to
answer, and how did you choose that question? Are your conclusions precise and
nuanced, as opposed to over-generalizations?

● Technical Expositions

o Wrangling & Cleaning Process. Did you conduct proper quality control and
handle common error types? How did you transform the datasets to better use
them together? What sorts of feature engineering did you perform? Please
describe your process in detail within your Report.

o Investigative Depth. How did you conduct your exploratory data analysis (EDA)
process? What other hypothesis tests and ad-hoc studies did you perform, and
how did you interpret the results of those tests and analyses? What patterns did
you notice, and how did you use these to make subsequent decisions?

o Analytics & Modeling Rigor. What assumptions and choices did you make, and
how did you justify them? How did you perform feature selection? If you build
models, how did you analyze their performance, and what shortcomings do they
exhibit? If you constructed visualizations and/or conducted statistical tests, what
was the motivation behind the particular models you build, and what did you tell
you?