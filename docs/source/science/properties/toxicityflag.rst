Toxicity flag
=============
Unit: [True/False] (True: contains a toxical substructure | False: does not contain a toxical substructure)

Organic electronic devices have potential applications ranging from light emitting devices (in-door and out-door as well), devices operating in extreme conditions to wearable devices that are in constant contact with our skin, or even medical devices that can be within our body.
But even if a simple coating of a surface is considered, humans can interact with these materials, thus their effect on health can be a source of issues in the future.
In the field of drug discovery, the evaluation of toxicity in the in-silico phase is a general step, although precise prediction of toxic behaviour through metabolism is a complex process.
Based on the experimental toxicity data of several investigated molecules, there are already identified substructural patterns and functional groups that can always be associated with toxic effects, regardless of the overall chemical structure.

ToxAlerts [1]_ is a web service to provide evaluation of possible toxic properties based on literature data, where toxicity is linked to substructural patterns, like functional groups.
Based on the collected literature data, generalized patterns are provided in SMARTS format.
Based on these SMARTS patterns we have **flagged** compounds matching these patterns and probably possessing toxical features.


.. [#] Iurii Sushko et al, J. Chem. Inf. Model. 2012, 52, 8, 2310–2316 https://pubs.acs.org/doi/10.1021/ci300245q
