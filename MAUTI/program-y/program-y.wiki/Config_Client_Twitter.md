# Twitter Client Configuration

In addition to the [common configuration items](./Config_Client) available to all clients, the additional configuration 
items available to a Twiiter client are as follows

```yaml
twitter:
  polling: true
  polling_interval: 49
  streaming: false
  use_status: true
  use_direct_message: true
  auto_follow: true
  storage: file
  storage_location: $BOT_ROOT/storage/twitter.data
  welcome_message: Thanks for following me, send me a message and I'll try and help
```

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Example</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>polling</td>
    <td>Use tweepy polling mechanism</td>
    <td>[True|False]</td>
    <td>True</td>
  </tr>
  <tr>
    <td>polling_interval</td>
    <td>Number of seconds to wait between polling Twitter for new messages</td>
    <td>60</td>
    <td>49</td>
  </tr>
  <tr>
    <td>streaming</td>
    <td>Use tweepy streaming - Note at this stage this is not supported</td>
    <td>[True|False]</td>
    <td>False</td>
  </tr>
  <tr>
    <td>use_status</td>
    <td>When polling, query for all new status updates</td>
    <td>[True|False]</td>
    <td>True</td>
  </tr>
  <tr>
    <td>use_direct_message</td>
    <td>When polling, query for all new direct messages</td>
    <td>[True|False]</td>
    <td>True</td>
  </tr>
  <tr>
    <td>auto_follow</td>
    <td>Follow back any user that follows this account</td>
    <td>[True|False]</td>
    <td>True</td>
  </tr>
  <tr>
    <td>storage</td>
    <td>Store current status and direct message id so as not to ask for old ones</td>
    <td>file</td>
    <td>file</td>
  </tr>
  <tr>
    <td>storage_location</td>
    <td>Where to store status and direct message file</td>
    <td>/tmp/twitter.txt</td>
    <td></td>
  </tr>
  <tr>
    <td>welcome_message</td>
    <td>If auto follow is on, what message should be sent back after following the user back</td>
    <td>Thanks for following me.</td>
    <td>Thanks for following me, send me a message and I'll try and help</td>
  </tr>
</table>