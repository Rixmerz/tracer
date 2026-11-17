# Client content inventory

Every piece of content the client gave, before any design. Kept in
`docs/tracer/content.md`. The builder never adds a statement of fact that is
not here: a missing fact is a question to the client, not text on screen.

```markdown
Source: <file, message or document, with its date>
Complete? yes / no: <where it is cut or what is missing>

| Id | Text (as given) | Kind (literal / free) | Where it goes | Requirement |
| --- | --- | --- | --- | --- |
| C1 | Solicitar consulta | literal: call to action | Primary button, every screen | REQ-cta |
| C2 | Más de 40 años de trayectoria | literal: claim | Home | REQ-home-claims |
| C3 | <service list> | free: may be grouped, not reworded | Services | REQ-services |

Literal: shown word for word; only the client changes it.
Free: may be grouped, ordered or shortened, never given new facts.

Questions for the client:
| Question | Why it matters | Asked on | Answer |
| --- | --- | --- | --- |
```

Each literal line becomes a scenario:

```markdown
#### Scenario: the call to action is the client's
- WHEN any screen renders
- THEN the primary button reads "Solicitar consulta"
- WORKS: the button text equals content C1
- CORRECT: the person reads exactly the client's words, in every width
```
