# InfraHub Wish List

New strategy - tactical for AC3

Use Infrahub as data source only.  Forget about developing and or loading schemas.  As a run of the mill network engineer, I should expect the data to be there in a fully functional and operational server that has been stood up by SAs, DBAs, Software Developers.

## Start Infrahub & SuzieQ

```bash
uv run invoke start
```

## Load Schema & Menus

```bash
uv run invoke load-schema
```

## Load Bootstrap Data

```bash
uv run invoke load-data
```

## Load Transformations from git repo

```graphql
mutation AddRepository {
  CoreReadOnlyRepositoryCreate(
    data: {name: {value: "ac3"}, location: {value: "https://github.com/BeArchiTek/infrahub_ac3_schema.git"}}
  ) {
    ok
    object {
      id
    }
  }
}
```

## Priority 2

Figure out how to create an artifact 100% within infrahub.

Add a new MLAG Pair prg-core1, pro-core2 (eos)
Add an Arista template (how does Infrahub handle template modularity?)

Generate corresponding configuration artifacts for both switches.

## Priority 3 (unlikely for AC3 )

Campus could leverage dcim.yml but also needs things like Access Points.  Could we use Physical Device for Appliance..probably but something feels right about breaking it out.
Appliances:

- deep packet inspection appliances
- firewalls
- wlcs
- ups
- management appliances

Does wireless need its own?  APs specifically?

### Structured Cabling

![structured_cabling_example](images/structured_cabling_example.png)

### Design Rationale

- **`CablingRun`** is the core entity describing the physical characteristics of the run.
- **`TerminationPoint`** is a reusable node that represents each end of a cable.
- **Edges** connect a cabling run to one or more termination points, accommodating flexibility (e.g., MPO trunks or split runs).
- **Connector types** and **housing types** are standardized through dropdowns to avoid inconsistency.
- Optional attributes (like `innerduct`) allow capturing pathway metadata without requiring it.


Racks and Power are next