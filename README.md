# general-server-assistant

#### [English](README.md) [简体中文](README-cn.md)

#### The Gsetant project aims to provide a set of enhancements features for the current popular media servers (Plex, Emby, Jellyfin), using APIs and plug-ins to integrate with the media server and provide functional extensions.

#### Gsetant has a complete API and architecture and supports the integration of more functions into the Gsetant platform through plug-ins. The detailed plug-in list can be found in other projects in the organization

## Instructions for use

### Use public Gsetant

#### The community host a public Gsetant server. You can register and use the public Gsetant provided by the community by visiting https://www.gsetant.xyz
#### However, you still need to install the plugin of Gsetant to you media server ([Plex](https://github.com/gsetant/Gsetant.bundle), [Emby(release soon)](), [Jellyfin(release soon)]())
#### If you like Gsetant, please star this project
#### [Join our Telegram group to ask any questions](https://t.me/AdultScraperX) 
### Self-deployment

#### Gsetant recommends using docker for deployment. For deployment details, please refer to the following [Address](https://github.com/gsetant/general-server-assistant/tree/master/docker)

#### [Gsetant for Synology](doc/Synology/Readme.md) (Thanks for Leo to provide this documnet)
#### The initial installation of Gsetant platform does not install any service plug-ins by default. Users need to install them on demand. Gsetant provides one-click installation function. Please refer to the specific plug-in description.

### Supported Plugin list

| Plugin                                                                            | Description                                              |
| -----------                                                                       | -----------                                              |
| [Adultscraperx](https://github.com/gsetant/adultscraperx)                         | A adult content metadata agent                           |
| [NeteaseCloudMusic](https://github.com/gsetant/NeteaseCloudMusic)                 | A Netease cloud music metadata agent                     |
| [MDTV](https://github.com/gsetant/mdtv)                                           | A model media metadata agent                             |