import time


class UniqueMonotonicCodeGenerator:
    def _generate_monotonic_codes(self):
        time_monotonic_codes = []
        for index in range(3660):
            time_monotonic_codes.append(str(time.monotonic_ns())[4:10])
        time_monotonic_codes = [
            time_monotonic_codes[0], time_monotonic_codes[3659]]
        return time_monotonic_codes

    def _generate_unique_monotonic_code(self):
        time_monotonic_codes = self._generate_monotonic_codes()
        if time_monotonic_codes[0] == time_monotonic_codes[1]:
            self._generate_unique_monotonic_code()
        return time_monotonic_codes[1]

    def generate(self):
        return self._generate_unique_monotonic_code()
