Feature: Get Artists

  Scenario Outline: Get Spotify catalog information for a single artist identified by their unique Spotify ID.
     Given the endpoint artists
     And id <resource_id>
     When method get
     Then the response status is <response_status>
     And the response matches <response_schema> schema

     Examples:
       | resource_id             | response_status | response_schema              |
       | 5eAWCfyUhZtHHtBdNk56l1  | 200             | get-artist-by-id-schema.json |
       | invalid                 | 400             | bad-request-schema.json      |