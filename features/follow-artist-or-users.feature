Feature: Follow Artists or Users

  Scenario Outline: Add the current user as a follower of one or more artists or other Spotify users [FOUND]
     Given the endpoint me/following
     And param ids <resource_id>
     And param type <type>
     When method put with params
     Then the response status is <response_status>

    Examples:
       | resource_id                  | type   | response_status |
       | 5eAWCfyUhZtHHtBdNk56l1       | artist | 204             |
       | spotify                      | user   | 204             |

     Scenario Outline: Add the current user as a follower of one or more artists or other Spotify users. [ERROR]
     Given the endpoint me/following
     And param ids <resource_id>
     And param type <type>
     When method put with params
     Then the response status is <response_status>
     And the response equals <response_json> json

     Examples:
       | resource_id                  | type   | response_status | response_json             |
       | invalid                      | artist | 400             | invalid-artist-id.json    |
       | invalid                      | user   | 400             | invalid-user-id.json      |