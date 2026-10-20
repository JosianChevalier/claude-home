# Working on the harness

Loaded only when this repo is the working directory, not when it serves as home.

- Trunk-based: `main` is the only line. In a cloud session each commit is fast-forwarded onto `main` as it lands (`git push origin HEAD:main`); the session branch never carries what `main` does not.
- A change is committed the moment it is made; the commit waits only on a doubt worth raising to the user.
- A harness file is live as soon as it is edited in its folder. A draft that could impact other real work while still wrong is held in the work file (`ongoing-work`) until settled, then moved in place.
