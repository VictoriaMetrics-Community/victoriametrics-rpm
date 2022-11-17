[![GitHub license](https://img.shields.io/github/license/VictoriaMetrics/VictoriaMetrics.svg)](https://github.com/VictoriaMetrics/victoriam-metrics-rpm/blob/master/LICENSE)
[![Slack](https://img.shields.io/badge/join%20slack-%23victoriametrics-brightgreen.svg)](https://slack.victoriametrics.com/) <a href="https://twitter.com/VictoriaMetrics"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/VictoriaMetrics?style=social"></a> <a href="https://www.reddit.com/r/VictoriaMetrics/"><img alt="Subreddit subscribers" src="https://img.shields.io/reddit/subreddit-subscribers/VictoriaMetrics?style=social"></a>

# victoriametrics-rpm
RPM for VictoriaMetrics LTS - fast, cost-effective monitoring solution and time series database

| Package | Status |
| ------- | ------ |
| vmsingle | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmsingle/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmsingle/) |
| vmagent | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmagent/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmagent/) |
| vmalert | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmalert/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmalert/) |
| vmauth | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmauth/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmauth/)|
| vmbackup | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmbackup/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmbackup/) |
| vmctl | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmctl/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmctl/) |
| vminsert | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vminsert/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vminsert/) |
| vmrestore | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmrestore/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmrestore/) |
| vmselect | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmselect/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmselect/) |
| vmstorage | [![Copr build status](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmstorage/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/denisgolius/VictoriaMetrics-LTS-rpm/package/vmstorage/) |

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
sudo dnf -y copr enable denisgolius/VictoriaMetrics-LTS-rpm
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
sudo yum -y copr enable denisgolius/VictoriaMetrics
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