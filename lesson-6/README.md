# Lesson 6: Configure OpenTelemetry logging SDK in Python

In the previous tutorials, we have seen how to manually create spans in a Python application. In this tutorial, we will look at how to configure OTel logging SDK in Python application.

The OpenTelemetry SDK provides a handler that can be used to transport logs to any OTLP compatible backend. The following code snippets show how to configure the OTel logging SDK in a Python application.

### Configure the logging SDK

```python
import logging
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter,
)
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

logger_provider = LoggerProvider()
set_logger_provider(logger_provider)

exporter = OTLPLogExporter()
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)

# Attach OTLP handler to root logger
logging.getLogger().addHandler(handler)
```

In the above code snippet, a handler is created using the `LoggingHandler` class. The handler is attached to the root logger using the `addHandler()` method. The handler receives log records from the logger and sends them to the OTLP backend using the `OTLPLogExporter`.

## See your logs in SigNoz

<screenshots showing exact logs that was created with manual instrumentation>

## Next Steps

In this tutorial, we configured the Python application to send logs to SigNoz using the OpenTelemetry logging SDK.

In the [next lesson](https://github.com/SigNoz/opentelemetry-python-example/tree/main/lesson-7), we will learn how to customize metrics stream produced by OpenTelemetry SDK using views.
