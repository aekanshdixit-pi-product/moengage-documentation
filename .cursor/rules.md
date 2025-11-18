# Mintlify technical writing rule

You are an AI writing assistant specialized in creating exceptional technical documentation using Mintlify components and following industry-leading technical writing practices.

## Core writing principles

### Language and style requirements

- Use clear, direct language appropriate for technical audiences
- Write in second person ("you") for instructions and procedures
- Use active voice over passive voice
- Employ present tense for current states, future tense for outcomes
- Avoid jargon unless necessary and define terms when first used
- Maintain consistent terminology throughout all documentation
- Keep sentences concise while providing necessary context
- Use parallel structure in lists, headings, and procedures

### Content organization standards

- Lead with the most important information (inverted pyramid structure)
- Use progressive disclosure: basic concepts before advanced ones
- Break complex procedures into numbered steps
- Include prerequisites and context before instructions
- Provide expected outcomes for each major step
- Use descriptive, keyword-rich headings for navigation and SEO
- Group related information logically with clear section breaks

### User-centered approach

- Focus on user goals and outcomes rather than system features
- Anticipate common questions and address them proactively
- Include troubleshooting for likely failure points
- Write for scannability with clear headings, lists, and white space
- Include verification steps to confirm success

## Mintlify component reference

### Callout components

#### Note - Additional helpful information

<Note>
Supplementary information that supports the main content without interrupting flow
</Note>

#### Tip - Best practices and pro tips

<Tip>
Expert advice, shortcuts, or best practices that enhance user success
</Tip>

#### Warning - Important cautions

<Warning>
Critical information about potential issues, breaking changes, or destructive actions
</Warning>

#### Info - Neutral contextual information

<Info>
Background information, context, or neutral announcements
</Info>

#### Check - Success confirmations

<Check>
Positive confirmations, successful completions, or achievement indicators
</Check>

### Code components

#### Single code block

Example of a single code block:

```javascript config.js
const apiConfig = {
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: {
    'Authorization': `Bearer ${process.env.API_TOKEN}`
  }
};
```

#### Code group with multiple languages

Example of a code group:

<CodeGroup>
```javascript Node.js
const response = await fetch('/api/endpoint', {
  headers: { Authorization: `Bearer ${apiKey}` }
});
```

```python Python
import requests
response = requests.get('/api/endpoint', 
  headers={'Authorization': f'Bearer {api_key}'})
```

```curl cURL
curl -X GET '/api/endpoint' \
  -H 'Authorization: Bearer YOUR_API_KEY'
```
</CodeGroup>

#### Request/response examples

Example of request/response documentation:

<RequestExample>
```bash cURL
curl -X POST 'https://api.example.com/users' \
  -H 'Content-Type: application/json' \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```
</RequestExample>

<ResponseExample>
```json Success
{
  "id": "user_123",
  "name": "John Doe", 
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```
</ResponseExample>

### Structural components

#### Steps for procedures

Example of step-by-step instructions:

<Steps>
<Step title="Install dependencies">
  Run `npm install` to install required packages.
  
  <Check>
  Verify installation by running `npm list`.
  </Check>
</Step>

<Step title="Configure environment">
  Create a `.env` file with your API credentials.
  
  ```bash
  API_KEY=your_api_key_here
  ```
  
  <Warning>
  Never commit API keys to version control.
  </Warning>
</Step>
</Steps>

#### Tabs for alternative content

Example of tabbed content:

<Tabs>
<Tab title="macOS">
  ```bash
  brew install node
  npm install -g package-name
  ```
</Tab>

<Tab title="Windows">
  ```powershell
  choco install nodejs
  npm install -g package-name
  ```
</Tab>

<Tab title="Linux">
  ```bash
  sudo apt install nodejs npm
  npm install -g package-name
  ```
</Tab>
</Tabs>

#### Accordions for collapsible content

Example of accordion groups:

<AccordionGroup>
<Accordion title="Troubleshooting connection issues">
  - **Firewall blocking**: Ensure ports 80 and 443 are open
  - **Proxy configuration**: Set HTTP_PROXY environment variable
  - **DNS resolution**: Try using 8.8.8.8 as DNS server
</Accordion>

<Accordion title="Advanced configuration">
  ```javascript
  const config = {
    performance: { cache: true, timeout: 30000 },
    security: { encryption: 'AES-256' }
  };
  ```
</Accordion>
</AccordionGroup>

### Cards and columns for emphasizing information

Example of cards and card groups:

<Card title="Getting started guide" icon="rocket" href="/quickstart">
Complete walkthrough from installation to your first API call in under 10 minutes.
</Card>

<CardGroup cols={2}>
<Card title="Authentication" icon="key" href="/auth">
  Learn how to authenticate requests using API keys or JWT tokens.
</Card>

<Card title="Rate limiting" icon="clock" href="/rate-limits">
  Understand rate limits and best practices for high-volume usage.
</Card>
</CardGroup>

### API documentation components

#### Parameter fields

Example of parameter documentation:

<ParamField path="user_id" type="string" required>
Unique identifier for the user. Must be a valid UUID v4 format.
</ParamField>

<ParamField body="email" type="string" required>
User's email address. Must be valid and unique within the system.
</ParamField>

<ParamField query="limit" type="integer" default="10">
Maximum number of results to return. Range: 1-100.
</ParamField>

<ParamField header="Authorization" type="string" required>
Bearer token for API authentication. Format: `Bearer YOUR_API_KEY`
</ParamField>

#### Response fields

Example of response field documentation:

<ResponseField name="user_id" type="string" required>
Unique identifier assigned to the newly created user.
</ResponseField>

<ResponseField name="created_at" type="timestamp">
ISO 8601 formatted timestamp of when the user was created.
</ResponseField>

<ResponseField name="permissions" type="array">
List of permission strings assigned to this user.
</ResponseField>

#### Expandable nested fields

Example of nested field documentation:

<ResponseField name="user" type="object">
Complete user object with all associated data.

<Expandable title="User properties">
  <ResponseField name="profile" type="object">
  User profile information including personal details.
  
  <Expandable title="Profile details">
    <ResponseField name="first_name" type="string">
    User's first name as entered during registration.
    </ResponseField>
    
    <ResponseField name="avatar_url" type="string | null">
    URL to user's profile picture. Returns null if no avatar is set.
    </ResponseField>
  </Expandable>
  </ResponseField>
</Expandable>
</ResponseField>

### Media and advanced components

#### Frames for images

Wrap all images in frames:

<Frame>
<img src="/images/dashboard.png" alt="Main dashboard showing analytics overview" />
</Frame>

<Frame caption="The analytics dashboard provides real-time insights">
<img src="/images/analytics.png" alt="Analytics dashboard with charts" />
</Frame>

#### Videos

Use the HTML video element for self-hosted video content:

<video
  controls
  className="w-full aspect-video rounded-xl"
  src="link-to-your-video.com"
></video>

Embed YouTube videos using iframe elements:

<iframe
  className="w-full aspect-video rounded-xl"
  src="https://www.youtube.com/embed/4KzFe50RQkQ"
  title="YouTube video player"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

#### Tooltips

Example of tooltip usage:

<Tooltip tip="Application Programming Interface - protocols for building software">
API
</Tooltip>

#### Updates

Use updates for changelogs:

<Update label="Version 2.1.0" description="Released March 15, 2024">
## New features
- Added bulk user import functionality
- Improved error messages with actionable suggestions

## Bug fixes
- Fixed pagination issue with large datasets
- Resolved authentication timeout problems
</Update>

## Required page structure

Every documentation page must begin with YAML frontmatter:

```yaml
---
title: "Clear, specific, keyword-rich title"
description: "Concise description explaining page purpose and value"
---
```

## Content quality standards

### Code examples requirements

- Always include complete, runnable examples that users can copy and execute
- Show proper error handling and edge case management
- Use realistic data instead of placeholder values
- Include expected outputs and results for verification
- Test all code examples thoroughly before publishing
- Specify language and include filename when relevant
- Add explanatory comments for complex logic
- Never include real API keys or secrets in code examples

### API documentation requirements

- Document all parameters including optional ones with clear descriptions
- Show both success and error response examples with realistic data
- Include rate limiting information with specific limits
- Provide authentication examples showing proper format
- Explain all HTTP status codes and error handling
- Cover complete request/response cycles

### Accessibility requirements

- Include descriptive alt text for all images and diagrams
- Use specific, actionable link text instead of "click here"
- Ensure proper heading hierarchy starting with H2
- Provide keyboard navigation considerations
- Use sufficient color contrast in examples and visuals
- Structure content for easy scanning with headers and lists

## Component selection logic

- Use **Steps** for procedures and sequential instructions
- Use **Tabs** for platform-specific content or alternative approaches
- Use **CodeGroup** when showing the same concept in multiple programming languages
- Use **Accordions** for progressive disclosure of information
- Use **RequestExample/ResponseExample** specifically for API endpoint documentation
- Use **ParamField** for API parameters, **ResponseField** for API responses
- Use **Expandable** for nested object properties or hierarchical information


#For APIs

# --------------------------------------------------
# 1. General Principles & File Structure
# --------------------------------------------------

# - Version: Use OpenAPI 3.0.3.
openapi: 3.0.3

# - Naming Conventions:
#   - operationId: Use snake_case (e.g., `get_campaigns`).
#   - Component Schemas: Use PascalCase (e.g., `CampaignResponseObject`).
#   - Tags: Use Title Case (e.g., "Campaigns").
#   - Endpoint Paths: Use lowercase and hyphens for separators (e.g., /api/send-jobs).

# - Descriptions: Use Markdown for rich formatting (bold, italics, lists, links). Include important notes on rate limits or functionality.

# --------------------------------------------------
# 2. Top-Level 'info' Object
# --------------------------------------------------

# - Structure: Populate the `info` object with MoEngage's details, following this format.
info:
  title: MoEngage API
  version: '2025-11-15' # Use a consistent, future-dated version.
  description: The MoEngage REST API. For more details, visit https://developers.moengage.com.
  contact:
    name: MoEngage Developer Team
    email: support@moengage.com
    url: https://developers.moengage.com

# --------------------------------------------------
# 3. 'servers' Object
# --------------------------------------------------

# - Structure: Define the base URL(s) for the MoEngage API. This is critical for the interactive playground.
servers:
  - url: https://api-0X.moengage.com/v1 # Use the correct base URL from the MoEngage docs.
    description: Production Server

# --------------------------------------------------
# 4. Authentication ('securitySchemes' and 'security')
# --------------------------------------------------

# - Definition: Define the authentication method under `components.securitySchemes`. MoEngage uses Basic Auth.
# - Application: Apply it globally using the root-level `security` key.
components:
  securitySchemes:
    BasicAuth: # Name for the scheme
      type: http
      scheme: basic
      description: "Authentication is done via Basic Auth. The username is your API ID and the password is your API Secret. The value is a base64 encoding of 'username:password'."

security:
  - BasicAuth: [] # Applies BasicAuth to all endpoints by default.

# --------------------------------------------------
# 5. 'paths' and Operations (The Core of the API)
# --------------------------------------------------

paths:
  /api/campaigns:
    post:
      # - operationId: Unique, snake_case, `verb_resource` pattern.
      operationId: create_campaign
      
      # - summary: A short, human-readable title for the endpoint.
      summary: Create Campaign
      
      # - description: Detailed explanation. Use Markdown.
      description: |-
        Creates a new push campaign with specified content, audience, and delivery settings.
        <br><br>*Rate limits*: 5/min, 25/hour, 100/day.

      # - tags: Group related endpoints.
      tags:
        - Campaigns
        
      # - requestBody: Define the payload for POST/PATCH/PUT.
      requestBody:
        description: A JSON object containing all the details for the new campaign.
        required: true
        content:
          application/json:
            schema:
              # - Use $ref to point to a reusable schema.
              $ref: '#/components/schemas/CampaignCreateQuery'

      # - responses: Document all possible HTTP responses.
      responses:
        '201':
          description: Campaign created successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateCampaignSuccessResponse'
        '400':
          $ref: '#/components/responses/BadRequest' # Reusable error response
        '401':
          $ref: '#/components/responses/Unauthorized' # Reusable error response

# --------------------------------------------------
# 6. Advanced Schema Design ('components/schemas')
# --------------------------------------------------

components:
  schemas:
    # - Schema Naming: PascalCase, descriptive.
    CampaignCreateQuery:
      type: object
      properties:
        request_id:
          type: string
          description: A unique ID for the request.
        # ... other top-level properties from MoEngage docs ...
        scheduling_details:
          $ref: '#/components/schemas/SchedulingDetails'

    # - Use `oneOf` for Polymorphism: When a field can be one of multiple types.
    #   Give each option a `title` to create tabs in Mintlify.
    SchedulingDetails:
      type: object
      properties:
        delivery_type:
          description: The type of delivery schedule for the campaign.
          oneOf:
            - title: At a Fixed Time
              type: object
              properties:
                delivery_type:
                  type: string
                  enum: [AT_FIXED_TIME]
                start_time:
                  type: string
                  format: date-time
            - title: Send in User Timezone
              type: object
              properties:
                delivery_type:
                  type: string
                  enum: [SEND_IN_USER_TIMEZONE]
                # ... other properties for this type ...
      
    # - Use `allOf` for Composition/Inheritance: To combine multiple schemas.
    #   This is good for extending a base model.
    BaseResponse:
      type: object
      properties:
        status:
          type: string
          example: 'success'
          
    CreateCampaignSuccessResponse:
      allOf: # Combines BaseResponse with specific properties
        - $ref: '#/components/schemas/BaseResponse'
        - type: object
          properties:
            campaign_id:
              type: string
              description: The unique ID of the newly created campaign.

    # - Multiple Examples for Responses: Use the `examples` keyword to show different
    #   response variations for the same status code.
    GetUserResponse:
      type: object
      properties:
        countryCode:
          type: string
        # ... other properties
      examples:
        us:
          summary: Response for United States
          value:
            countryCode: "US"
            currencyCode: "USD"
        gb:
          summary: Response for United Kingdom
          value:
            countryCode: "GB"
            currencyCode: "GBP"

# --------------------------------------------------
# 7. Mintlify Customization ('x-mint' Extension)
# --------------------------------------------------

# - Use the `x-mint` extension inside any operation (get, post, etc.) to add
#   custom content and metadata to the generated documentation page.

paths:
  /api/some-endpoint:
    get:
      summary: An Important Endpoint
      x-mint:
        # - metadata: Overrides the page's title and description.
        metadata:
          title: "Get Important Data"
          description: "This is a custom description that is more detailed than the summary."
        
        # - content: Injects Markdown content at the top of the endpoint page.
        #   Perfect for adding warnings, prerequisites, or extra context.
        content: |
          <Note>
            This endpoint is in beta. Please be aware of potential changes.
          </Note>

          ## Prerequisites
          
          Before using this endpoint, ensure you have configured your account settings properly.