Test data strategy: each test creates its own data with randomised
values and removes it on teardown. The environment is recreated
(docker compose down && up) before a full regression run to
guarantee a known baseline, since the system under test has no
reset endpoint.