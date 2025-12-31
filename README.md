WRP Platform — Reference Implementation (WRP-1)



STATUS: FROZEN

VERSION: v1.0.0



The WRP Platform is the official reference implementation of the

Witness Receipt Protocol (WRP-1).



WRP-1 defines a deterministic, content-agnostic receipt protocol

for cryptographic data sealing and verification.



Once frozen, WRP-1 SHALL NOT change.





WHAT IS WRP?



WRP defines a minimal, immutable rule set for creating and verifying

cryptographic receipts over arbitrary JSON payloads.



WRP does not interpret data.

WRP does not enforce policy.

WRP does not depend on external state.



WRP guarantees only one thing:



Given the same payload, the same receipt hash is produced forever.





CORE PROPERTIES (WRP-1)



\- Deterministic canonicalization

\- SHA-256 hashing

\- Offline verification

\- Content-agnostic payloads

\- Cross-platform reproducibility

\- No semantic drift





CANONICALIZATION RULES (WRP-1)



\- UTF-8 encoding

\- JSON objects sorted by key (lexicographically)

\- No insignificant whitespace

\- Arrays preserved in order

\- Deterministic number serialization

\- Canonical JSON hashed using SHA-256



These rules are permanently frozen for WRP-1.





API ENDPOINTS



CREATE RECEIPT



POST /api/receipt/create



Request:

{

&nbsp; "payload": {

&nbsp;   "any": "json",

&nbsp;   "is": \["allowed", true, 123]

&nbsp; }

}



Response includes:

\- schema\_version

\- receipt\_id

\- receipt\_hash

\- canonical

\- payload

\- created\_at





VERIFY RECEIPT



POST /api/receipt/verify



Request:

{

&nbsp; "payload": {

&nbsp;   "any": "json",

&nbsp;   "is": \["allowed", true, 123]

&nbsp; },

&nbsp; "receipt\_hash": "hex\_sha256"

}



Response:

{

&nbsp; "valid": true,

&nbsp; "computed\_hash": "hex\_sha256"

}



Verification is stateless and does not rely on database storage.





IMMUTABILITY GUARANTEE



WRP-1 is frozen permanently.



\- Canonicalization SHALL NOT change

\- Hashing SHALL NOT change

\- Existing receipts SHALL remain valid indefinitely



Any change requires a new schema version (e.g. WRP-2).





USE CASES



\- Audit trails

\- Compliance snapshots

\- Legal evidence sealing

\- AI training data provenance

\- Scientific experiment freezing

\- Financial decision proofs



WRP is domain-neutral by design.





LICENSE



MIT License





AUTHOR



Darwin N. Vallejos

Architect of WRP

WRP Platform — Reference Implementation (WRP-1)



STATUS: FROZEN

VERSION: v1.0.0



The WRP Platform is the official reference implementation of the

Witness Receipt Protocol (WRP-1).



WRP-1 defines a deterministic, content-agnostic receipt protocol

for cryptographic data sealing and verification.



Once frozen, WRP-1 SHALL NOT change.





WHAT IS WRP?



WRP defines a minimal, immutable rule set for creating and verifying

cryptographic receipts over arbitrary JSON payloads.



WRP does not interpret data.

WRP does not enforce policy.

WRP does not depend on external state.



WRP guarantees only one thing:



Given the same payload, the same receipt hash is produced forever.





CORE PROPERTIES (WRP-1)



\- Deterministic canonicalization

\- SHA-256 hashing

\- Offline verification

\- Content-agnostic payloads

\- Cross-platform reproducibility

\- No semantic drift





CANONICALIZATION RULES (WRP-1)



\- UTF-8 encoding

\- JSON objects sorted by key (lexicographically)

\- No insignificant whitespace

\- Arrays preserved in order

\- Deterministic number serialization

\- Canonical JSON hashed using SHA-256



These rules are permanently frozen for WRP-1.





API ENDPOINTS



CREATE RECEIPT



POST /api/receipt/create



Request:

{

&nbsp; "payload": {

&nbsp;   "any": "json",

&nbsp;   "is": \["allowed", true, 123]

&nbsp; }

}



Response includes:

\- schema\_version

\- receipt\_id

\- receipt\_hash

\- canonical

\- payload

\- created\_at





VERIFY RECEIPT



POST /api/receipt/verify



Request:

{

&nbsp; "payload": {

&nbsp;   "any": "json",

&nbsp;   "is": \["allowed", true, 123]

&nbsp; },

&nbsp; "receipt\_hash": "hex\_sha256"

}



Response:

{

&nbsp; "valid": true,

&nbsp; "computed\_hash": "hex\_sha256"

}



Verification is stateless and does not rely on database storage.





IMMUTABILITY GUARANTEE



WRP-1 is frozen permanently.



\- Canonicalization SHALL NOT change

\- Hashing SHALL NOT change

\- Existing receipts SHALL remain valid indefinitely



Any change requires a new schema version (e.g. WRP-2).





USE CASES



\- Audit trails

\- Compliance snapshots

\- Legal evidence sealing

\- AI training data provenance

\- Scientific experiment freezing

\- Financial decision proofs



WRP is domain-neutral by design.





LICENSE



MIT License





AUTHOR



Darwin N. Vallejos

Architect of WRP



