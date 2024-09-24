# debug_manager.py

from debug import LogLevel
import time

class DebugManager:
    def __init__(self, logfile='debug.log', log_level=LogLevel.INFO):
        self.logfile = logfile
        self.log_level = log_level
        self.messages = []
        self.level_flags = {
            LogLevel.ERROR: True,
            LogLevel.WARNING: True,
            LogLevel.INFO: True
        }
    def log(self, message, level=LogLevel.INFO):
        # Log a message with a given log level
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{self._level_str(level)}] {message}"
        self.messages.append(log_entry)

        # If the log level flag is set, write the message to the log file
        if self.level_flags.get(level, False):
            self.write_to_file(log_entry)

    def _write_to_file(self, log_entry):
        # Write a log entry to the log file
        with open(self.logfile, 'a') as file:
            file.write(log_entry + '\n')

    def set_level_flags(self, error_flag=True, warning_flag=True, info_flag=True):
        # Enable or disable individual log levels
        self.level_flags[LogLevel.ERROR] = error_flag
        self.level_flags[LogLevel.WARNING] = warning_flag
        self.level_flags[LogLevel.INFO] = info_flag

    def get_messages(self, level=None):
        # Return all messages, or only the ones based on the selected log level
        if level:
            return [msg for msg in self.messages if self._get_level_from_message(msg) == level]
        return self.messages
    
    def _level_str(self, level):
        # Convert the log level to a string
        if level == LogLevel.ERROR:
            return 'ERROR'
        elif level == LogLevel.WARNING:
            return 'WARNING'
        elif level == LogLevel.INFO:
            return 'INFO'
        
    def _get_level_from_message(self, message):
        # Extract the log level from a log message
        if 'ERROR' in message:
            return LogLevel.ERROR
        elif 'WARNING' in message:
            return LogLevel.WARNING
        elif 'INFO' in message:
            return LogLevel.INFO
        
        