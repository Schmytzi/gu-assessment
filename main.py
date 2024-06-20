
import pandas as pd
from email.message import EmailMessage
import smtplib
import click

# This is its own function because of indexing weirdness with pandas
def extract_origin(sample_name):
    """Extracts the origin from a given sample name"""
    return sample_name[1]

@click.command()
@click.argument('input', required=True, type=click.Path(exists=True))
@click.option('-e', '--email', help="E-mail address to send notification. If not specified, no e-mail will be sent")
@click.option('--smtp', 'smtp_server', default="localhost", help="SMTP server to use for e-mail delivery. Please host your own because I don't support authentication, yet", show_default=True)
def main(input, email, smtp_server):
    """This script checks a QC file (specified by INPUT) for high failure rates from single origins"""
    samples = pd.read_csv(input)
    samples['origin'] = [extract_origin(x) for x in samples['sample']]
    # Flag failed samples
    samples["failed"] = (samples["pct_covered_bases"] < 95) | (~samples["qc_pass"])
    # Let Pandas do the aggregation for us
    pivot = samples.pivot_table(index = "origin", columns="failed", values="sample", aggfunc="size")
    # This is correct, the column names in the pivot table are booleans
    pivot = pivot.rename(columns={True : 'fail', False : 'pass'})
    pivot['pct_fail'] = pivot['fail'] / (pivot['fail'] + pivot['pass']) * 100
    print("Number of passed and failed samples, and failure percentage")
    print(pivot.to_string())

    # Send a warning if failure rate for at least one origin is over 10% and we know where to send it
    if email is not None and any(pivot['pct_fail'] > 10):
        msg = EmailMessage()
        msg.set_content(f"At least one origin produced a high failure rate. See the following table:\n {pivot.to_string}")
        msg["Subject"] = "High failure rate in recent run"
        msg['From'] = "workflow@yourcluster"
        msg["To"] = email
        smtpclient = smtplib.SMTP(smtp_server)
        smtpclient.send_message(msg)
        smtpclient.close()

if __name__ == "__main__":
    main()