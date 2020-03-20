# Python Skeleton Application

Simple Python Flask application to test and debug your Nexmo credentials and environment. Utilise this application to test that your API credentials are in working order and to examine the event webhook data you receive when API requests are received by Nexmo from your account.

- [Requirements](#requirements)
- [Installation and Usage](#installation-and-usage)
  - [API Credentials](#api-credentials)
  - [Using ngrok](#using-ngrok)
  - [Running the Application](#running-the-application)
  - [Validate and Test your Credentials](#validate-and-test-your-credentials)
- [Contributing](#contributing)
- [License](#license)

## Requirements

This application requires that you have the following installed locally:

- [Python](https://www.python.org)
- [Flask](https://https://github.com/pallets/flask)
- [Nexmo Python Server SDK](https://github.com/Nexmo/nexmo-python)

Additionally, in order to test your Nexmo account, you must have a Nexmo account. You can create a Nexmo account for free or manage your Nexmo account details at the [Nexmo Dashboard](https://dashboard.nexmo.com).

## Installation and Usage

You can run this application by first cloning this repository locally:

```bash
git clone git@github.com:Nexmo/python-skeleton-app.git
```

Alternatively, you could also first fork your own copy of this repository to your GitHub profile and then clone your own forked copy.

Once you have downloaded a local copy, change into the directory of the application in your terminal. You can now set up the application for your Nexmo account.

### API Credentials

In order to test your API credentials, you need to init them first. From your terminal and inside the directory of the app just execute the **init.app.py** helper:

```bash
python helpers/init.app.py
```

Then supply the required info, at the end of this process a **.env** will automatically be created in your root folder.

The `NEXMO_API_KEY` and `NEXMO_API_SECRET` are to be provided with your API key and secret, respectively. The `NEXMO_NUMBER` is the number you wish the test SMS message to originate from. For example, this could be your [Nexmo provisioned virtual phone number](https://developer.nexmo.com/numbers/overview). The `TO_NUMBER` is the number you wish to send the test SMS message to. This could be your own cell phone number.

As always, make sure to not commit your sensitive API credential data to any public version control. If you are using Git, you can add the `.env` file to your `.gitignore` file to ensure that it is not committed.

### Validate and Test your credentials

After starting your environment variables, you can validate credentials with the `nexmo.ops.py` helper. In fact, you can send an sms to your phone just to be sure that everything is working properly.

So in your terminal, in the project directory execute:

```bash
python helpers/nexmo.ops.py
```

Then just select the option you want for testing.

### Using ngrok

In order to test the incoming webhook data from Nexmo, the Nexmo API needs an externally accessible URL to send that data to. A commonly used service for development and testing is ngrok. The service will provide you with an externally available web address that creates a secure tunnel to your local environment. The [Nexmo Developer Platform](https://developer.nexmo.com/concepts/guides/testing-with-ngrok) has a guide to getting started with testing with ngrok.

Once you have your ngrok URL, you can enter your [Nexmo Dashboard](https://dashboard.nexmo.com/settings) and supply it as `DELIVERY RECEIPTS` for any Nexmo service that sends data related with the message delivery via webhook. The Url format is similar to:

`#{ngrok URL}/webhooks/delivery`

Then using the endpoint `#{ngrok URL}/send-sms`, you can simulate sending an sms to your mobile and check the server webhook response in the **flask logs**

Another test case is creating a Voice application and providing the ngrok URL in the following format as the event url:

`#{ngrok URL}/webhooks/event`

You can then call your Nexmo Voice application, and with your skeleton application running you can observe the webhook data be received in real time for diagnosis of any issues and testing of your Nexmo account.

### Running the Application

Once you have your API credentials incorporated and your ngrok setup ready, you can go ahead and use this skeleton app. To start the application's server, run the following from the command line inside the directory of the app:

```bash
export FLASK_APP=app.py && python -m flask run
```

You can test your credentials or send an sms using the cli helper, but you can do it using the next **web application endpoints**:

`#{ngrok URL}/check-credentials`

`#{ngrok URL}/send-sms`

The skeleton app is also capable of receiving Nexmo API webhook data. As mentioned in the [Using ngrok](#using-ngrok) section above, a good candidate for that test is a Nexmo Voice application. From within your Nexmo dashboard you can create a Nexmo Voice application, provision a Nexmo virtual phone number and then link that number to your Voice application. Once you have ensured that your new Voice application's `EVENT URL` is `#{ngrok URL}/webhooks/event`, you can then give your Nexmo number a phone call. You should see the webhook data in your console in real time. For example, data for a ringing phone call will look like this:

```json
{:from=>"447700900000", :to=>"447700900000", :uuid=>"a123456789012345fbdsw", :conversation_uuid=>"CON-234567-fdsfs34-vfddfh-btger3-22345", :status=>"ringing", :direction=>"inbound", :timestamp=>"2020-01-07T11:24:49.478Z"}
```

For **SMS delivery endpoint** `#{ngrok URL}/webhooks/delivery` the output should be something like this: (Real details not shown. Obscured as: "[example]")

```python
ImmutableMultiDict([('msisdn', '[Your Number]'), ('to', '[Nexmo Number]'), ('network-code', '[XXXXX]'), ('messageId', '[Message ID]'), ('price', '[price]'), ('status', 'delivered'), ('scts', '[XXXXXXXX]'), ('err-code', '0'), ('api-key', '[Your API Key]'), ('message-timestamp', '2020-03-19 20:20:42')])
```

You can exit your application at anytime by holding down the CTRL and C keys on your keyboard.

## Contributing

We ❤️ contributions from everyone! [Bug reports](X), [bug fixes](X) and feedback on the application is always appreciated. Look at the [Contributor Guidelines](X) for more information and please follow the [GitHub Flow](https://guides.github.com/introduction/flow/index.html).

## License

This projet is under the [MIT License](LICENSE)
