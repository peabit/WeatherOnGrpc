namespace WeatherOnGrpc.Domain.CurrentWeatherInCityService;

public sealed record CurrentWeatherInCity(
    string City,
    int Temperature,
    string Description
);