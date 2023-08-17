using WeatherOnGrpc;
using WeatherOnGrpc.Domain.CurrentWeatherInCityService;
using WeatherOnGrpc.Infrastructure.CurrentWeatherInCityService;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<ICurrentWeatherService, OpenMeteoCurrentWeatherService>();

builder.Services.AddGrpc();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddProblemDetails();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapGrpcService<GrpcPort>();

app.MapGet(
    "api/weather/{&city}",
    async (ICurrentWeatherService currentWeatherService, string city) =>
    {
        var currentWeatherInCityResult = await currentWeatherService.GetAsync(city);
        return currentWeatherInCityResult.ToHttpResult();
    });

app.Run();