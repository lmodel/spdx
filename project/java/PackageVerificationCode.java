package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An SPDX version 2.X compatible verification method for software packages.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PackageVerificationCode extends IntegrityMethod {

  private String algorithm;
  private String hashValue;
  private List<String> packageVerificationCodeExcludedFile;


}