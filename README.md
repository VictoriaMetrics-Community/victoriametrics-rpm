# victoriametrics-rpm

<p align="center">
   <img src="logo.png" width="300" alt="Home Assistant Add-on VictoriaLogs Database for logs">
</p>

[![GitHub license](https://img.shields.io/github/license/VictoriaMetrics/VictoriaMetrics.svg)](https://github.com/VictoriaMetrics-Community/homeassistant-addon-victoriametrics/blob/main/LICENSE) [![Slack](https://img.shields.io/badge/join%20slack-%23victoriametrics-brightgreen.svg)](https://slack.victoriametrics.com/) [![Twitter Follow](https://img.shields.io/twitter/follow/VictoriaMetrics?style=social)](https://x.com/VictoriaMetrics) [![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/VictoriaMetrics?style=social)](https://www.reddit.com/r/VictoriaMetrics/) [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white)](https://t.me/VictoriaMetrics_en)

RPM for VictoriaMetrics - fast, cost-effective monitoring solution and time series database



| Package | Status |
| ------- | ------ |
| vmsingle | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmsingle/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmsingle/) |
| vmagent | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmagent/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmagent/) |
| vmalert | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmalert/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmalert/) |
| vmauth | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmauth/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmauth/)|
| vmbackup | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmbackup/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmbackup/) |
| vmctl | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmctl/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmctl/) |
| vminsert | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vminsert/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vminsert/) |
| vmrestore | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmrestore/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmrestore/) |
| vmselect | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmselect/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmselect/) |
| vmstorage | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmstorage/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaMetrics-LTS/package/vmstorage/) |

❗️ Please disable [Selinux](https://ru.wikipedia.org/wiki/SELinux) before run install or configure it for your own needs - see more [here](https://github.com/patsevanton/victoriametrics-rpm/issues/10).

## Supported systems: 
- RedHat linux 7/8/9
- CentOS linux7
- CentOS-stream linux 8/9
- Oracle linux 7/8
- Fedora linux 35/36/37
- OpenSUSE Leap & OpenSUSE Tumbleweed linux
- Mageia linux
- OpenMandriva linux

## How to install VictoriaMetrics with dnf

```
sudo dnf -y install yum-plugin-copr
sudo dnf -y copr enable victoriametrics/VictoriaMetrics-LTS-rpm
sudo dnf makecache
sudo dnf -y install vmsingle
sudo dnf -y install vmagent
sudo dnf -y install vmalert
sudo dnf -y install vmauth
sudo dnf -y install vmbackup
sudo dnf -y install vmctl
sudo dnf -y install vminsert
sudo dnf -y install vmrestore
sudo dnf -y install vmselect
sudo dnf -y install vmstorage
```

## How to install VictoriaMetrics with yum:

```
sudo yum -y install yum-plugin-copr
sudo yum -y copr enable victoriametrics/VictoriaMetrics
sudo yum makecache
sudo yum -y install vmsingle
sudo yum -y install vmagent
sudo yum -y install vmalert
sudo yum -y install vmauth
sudo yum -y install vmbackup
sudo yum -y install vmctl
sudo yum -y install vminsert
sudo yum -y install vmrestore
sudo yum -y install vmselect
sudo yum -y install vmstorage
```
## Useful links:

- [VictoriaMetrics Website](https://victoriametrics.com/)
- [Official documentation](https://docs.victoriametrics.com/)
- [Quick start](https://docs.victoriametrics.com/Quick-Start.html)
- [Supported Architectures](https://docs.victoriametrics.com/BestPractices.html#supported-architectures)
- [VictoriaMetrics best practices](https://docs.victoriametrics.com/BestPractices.html)
- [Official Grafana dashboards for VictoriaMetrics](https://grafana.com/orgs/victoriametrics)
- [Guides](https://docs.victoriametrics.com/guides/)
- [Helm Charts](https://github.com/VictoriaMetrics/helm-charts)
- [Operator for VictoriaMetrics](https://github.com/VictoriaMetrics/operator)
- [MetricsQL](https://docs.victoriametrics.com/MetricsQL.html)
- [F.A.Q.](https://docs.victoriametrics.com/FAQ.html)
- [Troubleshooting](https://docs.victoriametrics.com/Troubleshooting.html)

## VictoriaMetrics communities

- [Github](https://github.com/VictoriaMetrics/VictoriaMetrics)
- [Twitter](https://twitter.com/VictoriaMetrics)
- [Reddit](https://www.reddit.com/r/VictoriaMetrics/)
- [Slack](https://slack.victoriametrics.com/)
- [Telegram](https://t.me/VictoriaMetrics_en)
