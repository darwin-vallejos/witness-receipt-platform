Witness Receipt Protocol (WRP)



Status



WRP-1 — FROZEN



Core Principle



Evolution is allowed.

Mutation is forbidden.



Once a receipt is issued under a schema version,

its meaning, canonicalization, and hash are immutable forever.





WRP-1 Definition



A Witness Receipt is defined as:



Arbitrary JSON payload



Canonicalized deterministically



Hashed using SHA-256



Verifiable offline without external state





Canonicalization Rules (WRP-1)



UTF-8 encoding



Unicode NFC normalization



JSON objects sorted by key (lexicographically)



No insignificant whitespace



Arrays preserved in order



Numbers serialized deterministically



No floats requiring rounding interpretation





Receipt Fields (WRP-1)



Required:



schema\_version: "WRP-1"



payload: object



receipt\_hash: hex SHA-256





Optional (non-semantic):



receipt\_id



created\_at





Optional fields MUST NOT affect the hash.





Immutability Guarantee



For WRP-1:



The canonicalization algorithm SHALL NOT change



The hash algorithm SHALL NOT change



Existing receipts SHALL remain valid indefinitely





Any change REQUIRES a new schema\_version.





Version Policy



WRP-1 is frozen permanently.



Future versions must be published as:



WRP-2



WRP-3

etc.





Backward compatibility is mandatory.





Reference Implementation



This repository is the official reference implementation of WRP-1.

Witness Receipt Protocol (WRP)



Status



WRP-1 — FROZEN



Core Principle



Evolution is allowed.

Mutation is forbidden.



Once a receipt is issued under a schema version,

its meaning, canonicalization, and hash are immutable forever.





WRP-1 Definition



A Witness Receipt is defined as:



Arbitrary JSON payload



Canonicalized deterministically



Hashed using SHA-256



Verifiable offline without external state





Canonicalization Rules (WRP-1)



UTF-8 encoding



Unicode NFC normalization



JSON objects sorted by key (lexicographically)



No insignificant whitespace



Arrays preserved in order



Numbers serialized deterministically



No floats requiring rounding interpretation





Receipt Fields (WRP-1)



Required:



schema\_version: "WRP-1"



payload: object



receipt\_hash: hex SHA-256





Optional (non-semantic):



receipt\_id



created\_at





Optional fields MUST NOT affect the hash.





Immutability Guarantee



For WRP-1:



The canonicalization algorithm SHALL NOT change



The hash algorithm SHALL NOT change



Existing receipts SHALL remain valid indefinitely





Any change REQUIRES a new schema\_version.





Version Policy



WRP-1 is frozen permanently.



Future versions must be published as:



WRP-2



WRP-3

etc.





Backward compatibility is mandatory.





Reference Implementation



This repository is the official reference implementation of WRP-1.



