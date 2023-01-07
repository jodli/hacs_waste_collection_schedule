# Abfalltermine Fürth

Support for Stadt Fürth schedules provided by [abfallwirtschaft.fuerth.eu](https://www.abfallwirtschaft.fuerth.eu/) located in Bavaria, Germany.

## Configuration via configuration.yaml

```yaml
waste_collection_schedule:
  sources:
    - name: abfalltermine_fuerth_de
      args:
        id: ID
```

### Configuration Variables

**id**
*(integer) (required)*: The unique 8-digit identifier of your street and street number

## Example

```yaml
waste_collection_schedule:
  sources:
    - name: abfalltermine_fuerth_de
      args:
        id: 88851001
```

### How to get the source arguments

1. Open <https://www.abfallwirtschaft.fuerth.eu/)>.
2. Fill out the filter fields on the page.
3. Right click the button "Kalender ... drucken" and select "Copy link address". You should get something like this `https://www.abfallwirtschaft.fuerth.eu/pdfexport.php?adresse=88851001&jahr=2023`
4. Copy the number after `adresse=` to your configuration file.
