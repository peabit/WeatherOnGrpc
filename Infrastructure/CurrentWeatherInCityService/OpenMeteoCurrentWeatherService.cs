using OpenMeteo;
using WeatherOnGrpc.Domain.Common;
using WeatherOnGrpc.Domain.CurrentWeatherInCityService;

namespace WeatherOnGrpc.Infrastructure.CurrentWeatherInCityService;

public sealed class OpenMeteoCurrentWeatherService : ICurrentWeatherService
{
    private readonly OpenMeteoClient _client = new();
    
    public async Task<Result<CurrentWeatherInCity>> GetAsync(string city)
    {
        var weatherForecast = await _client.QueryAsync(city);

        if (weatherForecast?.CurrentWeather is null)
        {
            return Result<CurrentWeatherInCity>.Failed("Weather not found");
        }
        
        var srcCurrentWeather = weatherForecast.CurrentWeather;
        
        var currentWeatherInCity = new CurrentWeatherInCity(
            City: city,
            Temperature: (int)Math.Round(srcCurrentWeather.Temperature),
            Description: _client.WeathercodeToString((int)srcCurrentWeather.Weathercode)
        );

        return Result<CurrentWeatherInCity>.Ok(currentWeatherInCity);
    }
}